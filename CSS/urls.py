from django.urls import path
from .views import css

urlpatterns = [
    path('', css, name="css")
]