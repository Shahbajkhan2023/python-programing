from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_view, name='student_form'),
    path('thank-you/', views.thank_you_view, name='thank_you'),  # Add this line
]