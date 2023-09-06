from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from comptes.models import Structure



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
        Cosommable_interne = '001', _('Consommable interne')
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
    na_autre = models.CharField(max_length=255,null=True,blank=True)
    miseDiso = models.CharField(
        _("mise Dispo"),
        max_length=18,
        choices=MiseDispo.choices,
        default=MiseDispo.Cosommable_interne)
    md_autre = models.CharField(max_length=255,null=True,blank=True)
    affectationAchat = models.CharField(
        _("Affectation de l'Achat"),
        max_length=30,
        choices=AffectationAchat.choices,
        default=AffectationAchat.Famille_accés_internet)
    activee = models.BooleanField(_("activé"),default=True)
    validee = models.BooleanField(_("validé"),default=False)
    creee_le = models.DateTimeField(_("date de soumition"), default=timezone.now)
    modifee_le = models.DateTimeField(_("dernière modification"), default=timezone.now)
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True)
    departement = models.ForeignKey(Structure,on_delete=models.PROTECT,null=True)


    

    

