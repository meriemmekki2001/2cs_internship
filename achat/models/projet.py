from django.db import models
from comptes.models import User
class Project(models.Model):


    code_projet = models.CharField(max_length=20, null=False)
    nom_projet = models.CharField(max_length=255, null=False)
    chef_projet = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='element_chef', null=False)
    sponsor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='element_sponsor', null=False)
    compte_comptable_detail = models.ManyToManyField('CompteComptableDetails', related_name='list_compte_detail')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.nom_projet}"

