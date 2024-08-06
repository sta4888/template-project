from .views import *
from django.urls import path

app_name = 'fapp'


urlpatterns = [
    path('', index, name='index'),
    path('request/', request_attrs, name='request_attrs'),
]
