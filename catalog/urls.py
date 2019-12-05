from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doors/', views.DoorListView.as_view(), name='doors'),
    path('doors/requests/', views.RequestListView.as_view(), name='requested-doors'),

    path('doors/request/<int:pk>/update/<str:status>/', views.RequestUpdate.as_view(), name='request-update'),

    path('door/<int:pk>', views.DoorDetailView.as_view(), name='door-detail'),
    path('door/<int:pk>/request/', views.RequestDoorView.as_view(), name='door-request'),
    path('users/', views.UserListView.as_view(), name='users'),

    path('log/', views.InputListView.as_view(), name='external_input'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),


]