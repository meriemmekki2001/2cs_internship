from .models import PreDemande,Produit,Categorie,Fournisseur
from django.contrib import admin


class ProduitAdmiin(admin.TabularInline):
     model = Produit


@admin.register(PreDemande)
class PreDemandeAdmin(admin.ModelAdmin) :
    inlines = [ProduitAdmiin]
    list_display = ['id' ,'cree_par','creee_le' , 'departement' ,'destinationCompte' ,]
    list_per_page = 10
    search_fields = ['departement__istartswith','destinationCompte__istartswith']
    ordering = ['creee_le']

#     list_editable=['num_inscription' ,'spécialité' , 'filière' ,'etablissment']


admin.site.register(Categorie)

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin) :
    list_display = ['matricule' ,'nom','email' , 'telephone' ,'email' ,]
    list_per_page = 10
    search_fields = ['nom__istartswith']
    list_select_related = ['categorie' ]
#     list_editable=['num_inscription' ,'spécialité' , 'filière' ,'etablissment']











