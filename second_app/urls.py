from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('thanks/', lambda request: render(request, 'second_app/thanks.html'), name='thanks'),
]
