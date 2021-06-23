
from django.urls import path
from django.urls.conf import include
from .views import HomeView, GunsView
from . import views

urlpatterns = [
# Home page
path('', HomeView.as_view(), name='home'),
path('guns/', GunsView.as_view(), name='guns'),
#path('gun/<int:pk>', GunView.as_view(), name='gun'),
path('gun/<int:gun_id>/', views.gunview, name='gun'),
path('guns/add_gun/', views.AddGun, name='add_gun'),
path('gun/add_bullet/<int:gun_id>/', views.addbullet, name='add_bullet'),
path('gun/add_data/<int:bullet_id>/', views.add_data, name='add_data'),
path('gun/edit_data/<int:result_id>/', views.edit_data, name='edit_data'),
path('gun/delete_data/<int:result_id>/', views.delete_data, name='delete_data'),
path('gun/edit_data/add_velocity/<int:result_id>/', views.add_velocity, name='add_velocity'),
path('gun/edit_bullet/<int:bullet_id>/', views.edit_bullet, name='edit_bullet'),
path('gun/delete_bullet/<int:bullet_id>/', views.delete_bullet, name='delete_bullet'),
path('gun/graph/<int:bullet_id>/', views.view_graph, name='view_graph'),

#path('add_gun/', AddGun.as_view(), name='add_gun'),
]