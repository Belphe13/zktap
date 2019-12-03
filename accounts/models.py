from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# from django.urls import reverse
from django.urls import reverse


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[username_validator], error_messages={'unique': "A user with that username already exists.",},)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=75, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user_public_key = models.CharField(max_length=256, default='0')
    doors = models.ManyToManyField('catalog.Door', related_name='assigned_doors', null=True, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['last_name', 'first_name']

    # Methods
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.username}'
