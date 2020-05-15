from django.contrib import admin
from .views import main,abc
from django.urls import path

urlpatterns = [
    path('',main),
    path('abc',abc)
]
