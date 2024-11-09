from django.urls import path
from .views import homepage, about, quote, testimonial

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('get_quotation', quote, name='quote'),
    path('testimonial', testimonial, name='testimonial'),
]
