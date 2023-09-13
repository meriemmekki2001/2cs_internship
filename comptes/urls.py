from django.urls import path,include
import django.contrib.auth.urls
from . import views
from django.contrib.auth import views as auth_views


# app_name = "comptes"
urlpatterns = [
    path('', views.AccessDinied, name='access_denied'),
    path('deconnexion/', views.Logout, name='custom_logout'),
    path('connexion/', views.LoginView.as_view(), name='custom_login'),
    path('comptes/', include('django.contrib.auth.urls')),
  
]