from .views import *
from django.urls import path

app_name = 'useri'

urlpatterns = [
    path('', login, name='login'),
]


# регистрация без почты
# регистрация с отправкой почты
# регистрация с отправкой почты с помощью celery
# регистрация с отправкой почты в консоль