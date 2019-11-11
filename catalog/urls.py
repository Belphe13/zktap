from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doors/', views.DoorListView.as_view(), name='doors'),
    path('door/<int:pk>', views.DoorDetailView.as_view(), name='door-detail'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]