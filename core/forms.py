from django.forms import ModelForm
from .models import PreDemande

class PreDemandeForm(ModelForm):
    class Meta:
        model = PreDemande
        fields = "__all__"
        
form = PreDemandeForm()
