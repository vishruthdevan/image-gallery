from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('photo/delete/<str:pk>/', views.deletePhoto, name='delete'),
    path('cat/delete/', views.deleteCat, name='delete_cat'),
    path('add/', views.addPhoto, name='add'),

]
