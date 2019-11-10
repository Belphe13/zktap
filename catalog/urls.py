from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('doors/', views.DoorListView.as_view(), name='doors'),
]