from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter')
]