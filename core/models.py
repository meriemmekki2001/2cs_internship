from datetime import timezone
import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class PreDemande(models.Model):
    CHOICES = [
    ("Moyens généraux", "Moyens généraux"),
    ("Interco", "Interco"),
]
    nom_du_produit = models.CharField(_("nom du produit"),max_length=100)
    details = models.CharField(max_length=250)
    date_de_la_demande =  models.DateTimeField(_("date de la demande"), default=timezone.now)
    service = models.CharField(
        max_length=15,
        choices=CHOICES,
        default="Moyens généraux",
    )
    def __str__(self):
        return self.nom_du_produit

