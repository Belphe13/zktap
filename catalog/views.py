from django.shortcuts import render
from .models import Door, User

# Create your views here.
def index(request):
    #num_doors = Door.objects.all().count()
    return render(request, 'index.html')
