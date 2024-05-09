from django.urls import path
from .views import *
urlpatterns = [
    path('', study_list, name='study_list'),
    path('<int:pk>/', study_detail, name='study_detail'),
    path('create/', CreateStudy.as_view(), name='create'),
    path('edit/<int:pk>/', UpdateStudy.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudyView, name='delete')
]