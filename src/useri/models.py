from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='profile_pics')
    bio = models.TextField()


    def __str__(self):
        return self.user