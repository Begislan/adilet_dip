from django.urls import path
from .views import html

urlpatterns = [
    path('', html, name="html")
]