from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from comptes.models import User

class DemandeAchat(models.Model):

    class DestinationCompte(models.TextChoices):
        MGX = 'MGX', _('Moyens Généraux')
        INT = 'INT', _('Interconnexions')

   
    class NatureAchat(models.TextChoices):
        Investissement = '001', _('Investissement')
        Service = '002', _('Service')
        Consommable = '003', _('Consommable')
        Autre = '004', _('Autre')

    
    class MiseDispo(models.TextChoices):
        Cosommable_interne = '001', _('Cosommable interne')
        Revente_client = '002', _('Revente client')
        Stock = '003', _('Stock')
        Autre = '004', _('Autre')

    
    class AffectationAchat(models.TextChoices):
        Famille_accés_internet = '001', _('Famille accés internet')
        Famille_Communication_unifié = '002', _('Famille Communication unifié')
        Famille_CLOUD = '003', _('Famille CLOUD')

        Autre = '005', _('Autre')
   
    class StatutAchat(models.TextChoices):
        En_cours = '001', _('En cours')
        Clôturé = '003', _('Clôturé')
        Annulé= '002', _('Annulé')
        

    class DeviseCompte(models.TextChoices):
        autre = 'autre', _('----------')
        DZD = 'DZD', _('Dinars Algérienne')
        EUR = 'EUR', _('Euro')
        USD = 'USD', _('Dollar')

    class Dispo(models.TextChoices):
            OUI = 'OUI', _('DISPONIBLE')
            NON = 'NON', _('NON DISPONIBLE')



    
    
    DA_Code = models.CharField(max_length=50, default="_", blank=True)
    code_comptable = models.ForeignKey('CompteComptable', on_delete=models.DO_NOTHING, null=True)
    code_comptable_detail = models.ForeignKey('CompteComptableDetails', on_delete=models.DO_NOTHING, null=True)
    projet = models.ForeignKey('Project', on_delete=models.DO_NOTHING, null=True)
    destination_achat = models.CharField(choices=DestinationCompte.choices, max_length=128)
    nature_achat = models.CharField(choices=NatureAchat.choices, max_length=128)
    autre_nature_achat = models.CharField(max_length=255, null=True)
    mise_dispo = models.CharField(choices=MiseDispo.choices, max_length=128)
    autre_mise_dispo = models.CharField(max_length=255, null=True)
    affectation_achat = models.CharField(choices=AffectationAchat.choices, max_length=128)
    autre_affectation_achat = models.CharField(max_length=255, null=True)
    total_devis = models.DecimalField(max_digits=50, decimal_places=3,null=True)
    devise = models.CharField(max_length=40, choices = DeviseCompte.choices, default = DeviseCompte.autre)
    disponibilité=models.CharField(choices=Dispo.choices, max_length=20,default = Dispo.OUI)
    bon_commande = models.CharField(max_length=25, null=True)
    statut_achat = models.CharField(choices=StatutAchat.choices, max_length=128)
    detail_statut_achat = models.CharField(max_length=255, null=True)
    etat_achat = models.CharField(max_length=255, null=True)
    
    note_achat = models.TextField()
    validation_dg = models.BooleanField(default=False)
    autre_validation = models.TextField(default=False)
    validation_directeur = models.BooleanField(default=False)
    Date_valid_directeur = models.DateTimeField(null=True)
    Date_valid_dg = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='element_create')
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='element_update')
    



   
    

   

