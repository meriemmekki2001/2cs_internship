from django.db import models
from django.utils.translation import gettext_lazy as _


class PreDemande(models.Model):
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

    designation = models.CharField(_("Désignation"),max_length=250,null=False,blank=False)
    qtt = models.IntegerField(_("Quantité"),null=False,blank=False)
    destinationCompte = models.CharField(
        _("Compte de Destination"),
        max_length=15,
        choices=DestinationCompte.choices,
        default=DestinationCompte.MGX)
    natureAchat = models.CharField(
        _("Nature de l'Achat"),
        max_length=14,
        choices=NatureAchat.choices,
        default=NatureAchat.Investissement)
    miseDiso = models.CharField(
        max_length=18,
        choices=MiseDispo.choices,
        default=MiseDispo.Cosommable_interne)
    affectationAchat = models.CharField(
        _("Affectation de l'Achat"),
        max_length=30,
        choices=AffectationAchat.choices,
        default=AffectationAchat.Famille_accés_internet)
    
    def __str__(self):
        return self.designation

    
