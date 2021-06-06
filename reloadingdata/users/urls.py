
from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
# Home page
path('register/', UserRegistrationView.as_view(), name='register'),

]