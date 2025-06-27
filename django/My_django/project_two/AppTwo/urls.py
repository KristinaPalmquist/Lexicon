from django.urls import path
from first_project.first_app import views


urlpatterns = [
    path('index/', views.index, name='index')
]
