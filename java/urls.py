from django.urls import path
from java import views

urlpatterns = [
    path('', views.java, name="java")
]