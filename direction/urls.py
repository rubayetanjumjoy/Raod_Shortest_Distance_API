
from django.contrib import admin
from django.urls import path

from .apis import *

urlpatterns = [
    path('direction/', Direction.as_view(), name ='direction'),
]
