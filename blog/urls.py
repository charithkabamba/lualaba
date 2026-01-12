from django.urls import path

from .views import *

urlpatterns = [
    path('blog/', news ,name='news'),
    path('article/', article ,name='article'),
    path('all-news/', blog ,name='blog'),
]