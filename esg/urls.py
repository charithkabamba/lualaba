from django.urls import path

from .views import *

urlpatterns = [
    path('esg', esg, name='esg'),
    path('safety', safety, name='safety'),
]