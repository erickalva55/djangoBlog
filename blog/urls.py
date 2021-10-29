from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name="casa"),
    path('about', views.about, name="about"),
]
