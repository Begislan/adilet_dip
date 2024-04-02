from django.urls import path
from .views import javascript

urlpatterns = [
    path('', javascript, name="javascript")
]