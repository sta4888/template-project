# Настройка модели пользователя


### Существует несколько вариантов
- создасть модель ```profile``` и унаследоваться от модели ```User``` Django
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
``` 
но при этом нам нужно будет создать сигналы, чтоб при создании нового пользователя создавался и профиль для него
```python
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```
а чтоб сигнал заработал, в файле ```apps.py``` нашего приложения, мы должны добавить 
```python
def ready(self):
        import users.signals
```
- Создать ```CustomUser``` при этом мы копируем (расширяем) уже существующую модель, для этого в настройках мы указываем 
```python
AUTH_USER_MODEL = '<app_name>.<model_name>'
``` 
а в моделях мы создаем модель и наследуемся от ```AbstractUser``` 
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
```
так же мы меняем формы

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
```

- ```AbstractBaseUser```[здесь](https://stackoverflow.com/questions/21514354/abstractuser-vs-abstractbaseuser-in-django) дан подробный ответ и здесь

Если вам нужен полный контроль над моделью User, лучше использовать AbstractBaseUser, но если вы просто добавляете вещи к существующему пользователю, например, вы просто хотите добавить дополнительное поле, например, поле местоположения или любые другие данные профиля, тогда используйте AbstractUser.