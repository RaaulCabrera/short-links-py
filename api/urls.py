from django.urls import path
from . import views

urlpatterns = [
    path('', views.createShortURL, name='createShortURL'),
    path('<shortKey>', views.getOriginalURL, name='getOriginalURL')
]