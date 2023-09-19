from django.db import models
from django.utils.translation import gettext_lazy as _
from comptes.models import User
class GeneralHistoricalDetail(models.Model):
    
    historique = models.ForeignKey('GeneralHistorical', on_delete=models.DO_NOTHING, related_name='element_historique')
    champ =  models.CharField(max_length=250, null=False, unique=False)
    
    new_data = models.JSONField(dict) 
    old_data = models.JSONField(dict) 
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='element_create_by')
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='element_update_by')
    
    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    

    
