from django.urls import path
from api import views

urlpatterns = [
    path('guns/', views.guns_list),
    path('gun/<int:pk>/', views.gun_detail),
    path('data-create/<int:pk>/', views.result_create),
    path('data-update/<int:pk>/', views.result_update),
    path('data-delete/<int:pk>/', views.result_delete),
    
]