from django.forms import ModelForm, Textarea,SelectMultiple
from .models import PreDemande

class PreDemandeForm(ModelForm):
    class Meta:
        model = PreDemande
        fields = "__all__"
        # widgets = {
        #     "designation": Textarea(),
        #     "destinationCompte": SelectMultiple(attrs={"class":"form-select","aria-label":"Default select example" })

            
        # }
        

