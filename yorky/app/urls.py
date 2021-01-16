from django.urls import path
from . import views

urlpatterns = [
    path('yorky', views.yorky_specialist)
]
