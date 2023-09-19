from django.db import models
from django.core.exceptions import ValidationError

class CompteComptable(models.Model):

    def only_int(value):
        if value.isdigit()==False:
            raise ValidationError('ID contains characters')

    code_comptable = models.CharField(max_length=6, validators=[only_int], unique=True)
    nom_compte = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code_comptable} - {self.nom_compte}"