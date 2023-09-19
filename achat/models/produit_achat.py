from django.db import models


class ProductPurchase(models.Model):
    designation = models.CharField(max_length=255, null=False)
    quantite = models.FloatField()
    fournisseur = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=50, decimal_places=3)
    id_achat = models.ForeignKey('DemandeAchat', on_delete=models.DO_NOTHING, related_name='element_achat')
