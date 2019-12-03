from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.urls import reverse
from django.views.generic.base import View, TemplateView

from accounts.models import User
from .models import Door, DoorRequest, ExternalInput
from django.views import generic
from django.contrib import messages

# Create your views here.
def index(request):
    # Generate counts of some of the main objects
    num_doors = Door.objects.all().count()
    num_users = User.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_doors': num_doors,
        'num_users': num_users,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class DoorListView(generic.ListView):
    model = Door
    paginate_by = 10

    def get_queryset(self):
        queryset = Door.objects.all()
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            for door in queryset:
                setattr(door, 'request', DoorRequest.objects.filter(door=door, user=self.request.user).first())
        return queryset


class DoorDetailView(generic.DetailView):
    model = Door


class InputDetailView(generic.DetailView):
    model = ExternalInput


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'catalog/user_list.html'
    paginate_by = 10


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'catalog/user_detail.html'
    context_object_name = 'user_accessed'


class RequestDoorView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/request_door.html'

    def get(self, request, *args, **kwargs):
        try:
            door = Door.objects.filter(id=kwargs.get('pk')).first()
            DoorRequest.objects.get_or_create(door=door, user=self.request.user)
            return redirect(reverse('doors'))
        except Exception as e:
            print(e)
            return redirect(reverse('doors'))


class RequestListView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    model = DoorRequest
    paginate_by = 10
    template_name = 'catalog/requested_doors_list.html'
    context_object_name = 'door_requests'

    def test_func(self):
        return self.request.user.is_superuser


class RequestUpdate(UserPassesTestMixin, LoginRequiredMixin, TemplateView, ):
    model = DoorRequest
    template_name = 'catalog/requested_doors_list.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        try:
            door_request = DoorRequest.objects.filter(id=kwargs.get('pk')).first()
            if door_request:
                door_request.status = kwargs.get('status')
                door_request.save()
                if kwargs.get('status') == DoorRequest.APPROVED:
                    if door_request.door not in door_request.user.doors.all():
                        door_request.user.doors.add(door_request.door)
                elif kwargs.get('status') == DoorRequest.REJECTED:
                    door_request.user.doors.remove(door_request.door)
            return redirect(reverse('requested-doors'))
        except Exception as e:
            print(e)
            return redirect(reverse('requested-doors'))
