from django.urls import path
from .views import kotlin, kotlin_detail

urlpatterns = [
    path('', kotlin, name="kotlin"),
    path('<int:pk>/', kotlin_detail, name="kotlin_detail")
]