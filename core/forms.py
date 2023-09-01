from .models import PreDemande
from django.forms import ModelForm, Textarea,Select,NumberInput,TextInput

    


class PreDemandeForm(ModelForm):
    class Meta:
        model = PreDemande
        fields = "__all__"
        widgets = {
            "designation": Textarea(attrs={"class":"form-select","id":"exampleFormControlTextarea1","rows":"2" }),
            "qtt": TextInput(attrs={"type":"number", "class":"form-control", "name":"integerInput" ,"placeholder":"Ce champs doit être un entier" }),
            "destinationCompte": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "natureAchat": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "miseDiso": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "affectationAchat": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
           
            
        }
        

