from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from comptes.models import User


class DemandePaiment(models.Model):
    class ModePaiment(models.TextChoices):
        Espèce = '001', _('Espèce')
        Chèque = '002', _('Chèque')
        Virement= '003', _('Virement')
        

    Num_DP = models.CharField(max_length=50, default="*/2022", blank=True)
    demande_achat = models.ForeignKey('DemandeAchat', on_delete=models.DO_NOTHING, null=True)
    Num_fournisseur = models.CharField(max_length=50, default="0", blank=True)
    beneficiaire = models.CharField(max_length=250, default="xxx", blank=True)
    bon_commande = models.CharField(max_length=250, default="xxx", blank=True)
    num_facture = models.CharField(max_length=250, default="xxx", blank=True)
    montant_chiffre = models.DecimalField(max_digits=50, decimal_places=3, null=True)
    montant_lettres = models.CharField(max_length=250, default="xxx", blank=True)
    devise = models.CharField(max_length=40, default='DZD')
    mode_paiment = models.CharField(choices=ModePaiment.choices, max_length=20, default=ModePaiment.Espèce)
    Num_compte = models.CharField(max_length=80, default="xxx", blank=True)
    rib = models.CharField(max_length=80, default="xxx", blank=True)
    adresse = models.CharField(max_length=250, default="xxx", blank=True)
    swift = models.CharField(max_length=80, default="xxx", blank=True)
    objet_paiment = models.CharField(max_length=255, null=True)
    document_DP = models.FileField(upload_to='documents/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='create_by')
    









