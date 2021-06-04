from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
    ''' Model for creation Posts by User'''
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})


