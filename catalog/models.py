from django.db import models
# Used to generate urls by reversing the URL patterns
from django.urls import reverse 


class Door(models.Model):
    # Fields
    door_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    #user_list = models.ManyToManyField(User, help_text="List of Authorized Users")
    door_public_key = models.CharField(max_length=256)

    # Methods
    def get_absolute_url(self):
        return reverse('door-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.door_name


# Create your models here.
class User(models.Model):
    # Fields
    netid = models.CharField(max_length=100, null='True', help_text='What is your NetID?')
    first_name = models.CharField(max_length=100, default='DEFAULT')
    last_name = models.CharField(max_length=100, default='DEFAULT')
    user_public_key = models.CharField(max_length=256, default='DEFAULT')
    door = models.ManyToManyField(Door, related_name=None)


    # Order
    class Meta:
        ordering = ['last_name', 'first_name']

    # Methods
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

