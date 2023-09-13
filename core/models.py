from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from comptes.models import Structure
from django.core.validators import RegexValidator



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
    class Statut(models.TextChoices):
        EN_COURS = '001', _('En cours')
        ANNULEE = '002', _("Annulée par l'utilisateur")
        VALIDEE_DS = '003', _("Validée par le directeur de la structure")
        CLOTUREE = '004', _('Clôturée')
    class Reponse(models.TextChoices):
        REJETEE_DS = '001', _('Rejetée par le directeur de la structure')
        REJETE_SA = '002', _("Rejetée par le service d'achat")
        VALIDEE_SA = '003', _("Validée par le service d'achat")

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
    creee_le = models.DateTimeField(_("date de soumition"), default=timezone.now)
    modifee_le = models.DateTimeField(_("dernière modification"), default=timezone.now)
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True)
    departement = models.ForeignKey(Structure,on_delete=models.PROTECT,null=True)
    statut =  models.CharField(
        _("Statut"),
        max_length=40,
        choices=Statut.choices,
        default=Statut.EN_COURS)
    reponse_finale = models.CharField(
        _("Réponse finale"),
        max_length=40,
        choices=Reponse.choices,null=True,blank=True)


class Produit(models.Model):
    designation = models.CharField(_("Désignation"),max_length=250,null=False,blank=False)
    qtt = models.IntegerField(_("Quantité"),null=False,blank=False)
    pre_demande = models.ForeignKey(PreDemande,on_delete=models.CASCADE,related_name='produit')


class Categorie(models.Model):
    nom = models.CharField(_("Catégorie"),max_length=250,null=True,blank=True)
    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    matricule = models.CharField(_("Matricule"),null=False,blank=False,unique=True,max_length=20)
    nom = models.CharField(_("Nom du fournisseur"),null=False,blank=False,max_length=150)
    email = models.EmailField(_("E-mail"),unique=True)
    telephone = models.CharField(validators=[phone_regex], max_length=15,unique=True,blank=False)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='fournisseur',null=True,blank=True)




    

    

    

