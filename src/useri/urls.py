from .views import *
from django.urls import path

app_name = 'useri'

urlpatterns = [
    path('/', login, name='login'),
]
