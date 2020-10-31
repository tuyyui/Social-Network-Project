from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', lambda request: render(request, 'form.html')),
 
]
