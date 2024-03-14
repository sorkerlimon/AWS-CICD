from django.contrib import admin
from django.urls import path,include
from .views import jobapply

urlpatterns = [
    path('', jobapply,name='jobapply'),
    path('license/', license,name='license'),
]
