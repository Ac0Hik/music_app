from django.urls import path
from .views import mn

urlpatterns = [
    path('', mn),
]
