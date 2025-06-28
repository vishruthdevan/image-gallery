from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('photo/delete/<str:pk>/', views.deletePhoto, name='delete'),
    path('add/', views.addPhoto, name='add'),
]
