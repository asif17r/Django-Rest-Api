from django.urls import path
from . import views

urlpatterns = [
    path('dogs/', views.AllDogs.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', views.SingleDog.as_view(), name='dog-detail'),
    path('breeds/', views.AllBreeds.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', views.SingleBreed.as_view(), name='breed-detail'),
]