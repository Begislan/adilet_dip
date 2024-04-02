from django.urls import path
from .views import kotlin

urlpatterns = [
    path('', kotlin, name="kotlin")
]