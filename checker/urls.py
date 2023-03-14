from django.urls import path

from .views import *

urlpatterns = [
    path('check/', check_license, name="check")
]