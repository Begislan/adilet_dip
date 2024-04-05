from django.urls import path
from .views import cisharp, cisharp_detail


urlpatterns = [
    path('', cisharp, name="cisharp"),
    path('<int:pk>/', cisharp_detail, name="ci_detail")
]