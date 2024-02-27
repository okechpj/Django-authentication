# urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.registration, name='signup'),
    path('login', views.user_login,  name='login'),
    path('logout/', views.user_logout, name='logout'),

    
]
