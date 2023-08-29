from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path('create/', views.create_predemande, name='create_predemande'),
    path('list/', views.pre_demande_list, name='pre_demande_list'),
]