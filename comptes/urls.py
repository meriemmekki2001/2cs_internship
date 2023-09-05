from django.urls import path
import django.contrib.auth.urls
from . import views


app_name = "comptes"
urlpatterns = [
#     path('signup/', views.SignupView.as_view(), name='signup'),
    path('', views.Dashboard, name='dashboard'),
    path('logout/', views.Logout, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
  
]