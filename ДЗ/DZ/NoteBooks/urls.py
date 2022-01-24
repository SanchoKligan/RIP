from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details/<int:id>/', views.details),
    path('report/', views.report)
]
