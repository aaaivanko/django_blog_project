from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    '''
    Creating Custom User allow us to change
    information about users more easily
    '''
    age = models.PositiveIntegerField(null=True, blank=True)


User = get_user_model()


class Profile(models.Model):
    '''Creating profile image for User'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Image"

