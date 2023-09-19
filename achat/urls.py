from django.urls import path
from . import views
from .views.demande_achat import *


urlpatterns = [
    path('demandeachat/create/', DemandeAchatForm_, name='demandeachat_create'),
    path('demandeachat/ajax_load_detail/', ajax_load_detail, name='ajax_load_detail'),
    path('demandeachat/ajax_load_detail_projet/', ajax_load_detail_projet, name='ajax_load_detail_projet'),
    path('demandeachat/ajax_load_compte_comptable/', ajax_load_compte_comptable, name='ajax_load_compte_comptable'),
  
]