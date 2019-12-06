from django.db import models
# Used to generate urls by reversing the URL patterns
from django.urls import reverse

from accounts.models import User


class Door(models.Model):
    # Fields
    door_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    door_public_key = models.CharField(max_length=256, default='0')
    door_private_key = models.CharField(max_length=256, default='0')

    # Methods
    def get_absolute_url(self):
        return reverse('door-detail', args=[str(self.id)])

    def __str__(self):
        return self.door_name


class DoorRequest(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'

    STATUS = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    )
    status = models.CharField(max_length=50, choices=STATUS, default=PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    door = models.ForeignKey(Door, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.door.door_name}, {self.user.username}'

class Input(models.Model):
    input_auth = models.CharField(max_length=100, default='1')
    input_door_public_key = models.CharField(max_length=256, default='0')
    input_userr_public_key = models.CharField(max_length=256, default='0')

    def __str__(self):
        return self.input_auth

# # Create your models here.
# class User(models.Model):
#     # Fields
#     netid = models.CharField(max_length=100, null='True', help_text='What is your NetID?')
#     first_name = models.CharField(max_length=100, default='DEFAULT')
#     last_name = models.CharField(max_length=100, default='DEFAULT')
#     user_public_key = models.CharField(max_length=256, default='0')
#     door = models.ManyToManyField(Door, related_name=None)
#
#     # Order
#     class Meta:
#         ordering = ['last_name', 'first_name']
#
#     # Methods
#     def get_absolute_url(self):
#         return reverse('user-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return f'{self.last_name}, {self.first_name}'
