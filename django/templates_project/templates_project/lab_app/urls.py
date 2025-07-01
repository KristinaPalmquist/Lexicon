from django.urls import path
from lab_app import views


app_name = 'lab_app'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
   
]
