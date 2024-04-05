from django.urls import path
from python import views

urlpatterns = [
    path('', views.pyt, name='python'),
    path('<int:pk>/', views.detail_python, name='detail_python')
]