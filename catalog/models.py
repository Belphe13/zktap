from django.db import models

# Create your models here.
class User(models.Model):
    # Fields
    user_name = models.CharField(max_length=100, help_text='What is your name?')
    #email = models.EmailField(default='DEFAULT')
    #user_public_key = models.CharField(max_length=256, default='DEFAULT')

    # Methods
    def __str__(self):
        return self.user_name

class Door(models.Model):
    # Fields
    door_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    #user_list = models.ManyToManyField(User, help_text="List of Authorized Users")
    #door_public_key = models.CharField(max_length=256, default='DEFAULT')

    # Methods
    def __str__(self):
        return self.door_name
