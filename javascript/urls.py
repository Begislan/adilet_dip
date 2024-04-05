from django.urls import path
from .views import javascript, javascript_detail

urlpatterns = [
    path('', javascript, name="javascript"),
    path('<int:pk>', javascript_detail, name="javascript_detail")
]