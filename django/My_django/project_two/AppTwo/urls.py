from django.urls import path
from first_project.app_1 import views


urlpatterns = [
    path('index/', views.index, name='index')
]
