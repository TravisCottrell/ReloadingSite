
from django.urls import path
from django.urls.conf import include
from .views import HomeView, GunsView
from . import views

urlpatterns = [
path('', HomeView.as_view(), name='home'),
path('guns/', GunsView.as_view(), name='guns'),
path('gun/<int:gun_id>/', views.gunview, name='gun'),
path('guns/add_gun/', views.AddGun, name='add_gun'),
path('gun/add_bullet/<int:gun_id>/', views.addbullet, name='add_bullet'),
path('gun/edit_bullet/<int:bullet_id>/', views.edit_bullet, name='edit_bullet'),
path('gun/delete_bullet/<int:bullet_id>/', views.delete_bullet, name='delete_bullet'),
path('gun/graph/<int:bullet_id>/', views.view_graph, name='view_graph'),
]