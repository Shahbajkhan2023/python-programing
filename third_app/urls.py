from django.urls import path
from .views import contact_view
from django.shortcuts import render


urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('thanks/', lambda request: render(request, 'thanks.html'), name='thanks'),
]


