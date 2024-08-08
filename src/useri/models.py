from django.contrib.auth.models import User, AbstractUser
from django.db import models


# первая версия
class Profile(models.Model):  # Это первый и самый простой вариант
    user = models.OneToOneField(to='CustomUser', on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='profile_pics')
    bio = models.TextField()

    def __str__(self):
        return self.user


# вторая версия
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user/avatars/', null=True)
    phone_number = models.CharField(max_length=18, default='', verbose_name='Номер телефона пользователя')


    def __str__(self):
        return self.email
