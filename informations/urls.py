from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    path('home/', lambda x : redirect('home')),
]