from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "core"
urlpatterns = [
    path('home/', views.index, name='index'),
    path('create/', views.create_pre_demande, name='create_predemande'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    path('validation_ds/<int:id>/', views.validation_ds, name='validation_ds'),
    path('rejet_ds/<int:id>/', views.rejet_ds, name='rejet_ds'),
    path('validation_sa/<int:id>/', views.validation_sa, name='validation_sa'),
    path('rejet_sa/<int:id>/', views.rejet_sa, name='rejet_sa'),
    path('create_fournisseur/', views.create_fournisseur, name='create_fournisseur'),
    path('list_fournisseurs/', views.list_fournisseur, name='list_fournisseurs'),
    path('delete_fournisseur/<int:id>/', views.delete_fournisseur, name='delete_fournisseur'),
    path('create_categorie/', views.create_categorie, name='create_categorie'),
    path('list_categories/', views.list_categories, name='list_categories'),
    path('delete_categorie/<int:id>/', views.delete_categorie, name='delete_categorie'),
    path('annuler_pda/<int:id>/', views.annuler_pda, name='annuler_pda'),

]

