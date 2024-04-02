from django.urls import path
from python import views

urlpatterns = [
    path('', views.pyt, name='python'),
]