from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('services/<int:pk>/', service_detail, name='service_detail'),
    path('contact/', contact, name='contact'),
    path('feature/', feature, name='feature'),
    path('success/', success, name='success'),
]