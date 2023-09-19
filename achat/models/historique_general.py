from django.db import models
from django.utils.translation import gettext_lazy as _
class GeneralHistorical(models.Model):
    

    table =  models.CharField(max_length=250, null=False, unique=False)
    id_enregistrement = models.CharField(max_length=250, null=False, unique=False) 
    action = models.CharField(max_length=250, null=False, unique=False)
   
    
    created_on = models.DateTimeField(auto_now_add=True)
    
