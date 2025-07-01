from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submissions/', views.submissions, name='submissions'),
    path('admin/', admin.site.urls),
]
