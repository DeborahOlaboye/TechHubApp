# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # List of blog posts
    path('<int:id>/', views.blog_detail, name='blog_detail'),  # Detail view for each blog post
]
