from django.urls import path
from java import views

urlpatterns = [
    path('', views.java, name="java"),
    path('<int:pk>/', views.java_detail, name="java_detail")
]