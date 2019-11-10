from django.shortcuts import render
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

