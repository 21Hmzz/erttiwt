from django.contrib import admin
from django.urls import path
from erttiwtFront import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
]