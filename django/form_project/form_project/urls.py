from django.contrib import admin
from django.urls import path
from form_app import views as form_views
from rating import views as rating_views

urlpatterns = [
    path('', form_views.index, name='index'),
    path('contact/', form_views.contact, name='contact'),
    path('submissions/', form_views.submissions, name='submissions'),
    path('admin/', admin.site.urls),
    path('review/', rating_views.review, name='review')
]
