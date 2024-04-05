from django.urls import path
from .views import html, html_detail

urlpatterns = [
    path('', html, name="html"),
    path('<int:pk>', html_detail, name="html_detail")
]