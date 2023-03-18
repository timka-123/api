from django.urls import path

from .views import create_temp_token, callback

urlpatterns = [
    path('create', create_temp_token, name='create'),
    path('callback', callback, name='callback')
]