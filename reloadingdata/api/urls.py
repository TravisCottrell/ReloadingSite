from django.urls import path
from api import views

urlpatterns = [
    path('guns/', views.guns_list),
    path('gun/<int:pk>/', views.gun_detail),
    
]