from django.urls import path
from .views import css,css_detail

urlpatterns = [
    path('', css, name="css"),
    path('<int:pk>', css_detail, name="css_detail")
]