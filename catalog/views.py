from django.shortcuts import render, get_object_or_404
from .models import Door, User
from django.views import generic

# Create your views here.
def index(request):
    # Generate counts of some of the main objects
    num_doors = Door.objects.all().count()
    num_users = User.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
            'num_doors':num_doors, 
            'num_users':num_users, 
            'num_visits':num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)

class DoorListView(generic.ListView):
    model = Door
    paginate_by = 10

class DoorDetailView(generic.DetailView):
    model = Door

class UserListView(generic.ListView):
    model = User
    paginate_by = 10

class UserDetailView(generic.DetailView):
    model = User
