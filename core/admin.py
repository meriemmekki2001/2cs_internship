from .models import PreDemande
from django.contrib import admin

@admin.register(PreDemande)
class PreDemandeAdmin(admin.ModelAdmin) :
    list_display = ["designation","qtt","destinationCompte","natureAchat","miseDiso","affectationAchat"]
    search_fields = ['designation__istartswith']
    ordering = [ "id" ]
    # list_select_related = ['user' ]
 


