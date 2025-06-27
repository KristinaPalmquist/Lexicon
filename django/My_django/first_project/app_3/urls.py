# from django.contrib import admin
from django.urls import path
from app_3 import views


urlpatterns = [
    path('users/', views.users, name='users'),
    # path('admin/', admin.site.urls),
]
