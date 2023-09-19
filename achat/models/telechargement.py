from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from comptes.models import User


class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='downloaded_by')
    demande_achat = models.ForeignKey('DemandeAchat', on_delete=models.DO_NOTHING, null=True)
    created_on = models.DateTimeField(auto_now_add=True)











