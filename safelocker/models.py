from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserLocker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=55)
    site_url = models.URLField()
    username = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.site_name} - {self.username}'
