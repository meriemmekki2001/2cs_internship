from django.db import models
from django.utils.translation import gettext_lazy as _
from comptes.models import Structure
class CompteComptableDetails(models.Model):
    class DestinationCompte(models.TextChoices):
        MGX = 'MGX', _('Moyens Généraux')
        INT = 'INT', _('Interconnexions')

    class DeviseCompte(models.TextChoices):
        DZD = 'DZD', _('Dinars Algérienne')
        EUR = 'EUR', _('Euro')  
        USD = 'USD', _('Dollar')

    class StatusDetail(models.TextChoices):
        Actif = 'Actif', _('Actif')
        Inactif = 'Inactif', _('Inactif')     

    code_comptable = models.ForeignKey('CompteComptable', on_delete=models.DO_NOTHING, related_name='compte_detail')
    code_detail = models.CharField(max_length=250,  unique=False) 
    budget = models.DecimalField(max_digits=50, decimal_places=2,  default = 0.00) 
    destination_achat_compte = models.CharField(max_length = 80, choices = DestinationCompte.choices, default = DestinationCompte.MGX)
    devise = models.CharField(max_length = 40, choices = DeviseCompte.choices, default = DeviseCompte.DZD)
    structure = models.ForeignKey(Structure, on_delete=models.DO_NOTHING, related_name='compte_direction', null=True)
    status = models.CharField(max_length = 40, choices = StatusDetail.choices, default = StatusDetail.Actif)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return f"{self.code_comptable} - {self.code_detail}"     