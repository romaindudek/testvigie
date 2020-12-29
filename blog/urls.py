from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='index'),
    path('home', views.blog_index, name='index'),
]