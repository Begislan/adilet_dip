from django.urls import path
from .views import cisharp


urlpatterns = [
    path('', cisharp, name="cisharp" )
]