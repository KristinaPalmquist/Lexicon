from django.urls import path
from signup_lab_app import views

app_name = 'signup_lab_app'

urlpatterns = [
    path('register/', views.register, name='register'),
]