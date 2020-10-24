from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminArea/', views.adminArea, name='adminArea'),
    path('allTrucks/', views.allTrucks, name='allTrucks'),
    path('addTruck/', views.addTruck, name='addTruck')
]