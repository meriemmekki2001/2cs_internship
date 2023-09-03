from .models import PreDemande
from django.forms import ModelForm, Textarea,Select,TextInput
from django import forms

    


class PreDemandeForm(ModelForm):
    class Meta:
        model = PreDemande
        fields = "__all__"
        widgets = {
            "designation": Textarea(attrs={"class":"form-select","rows":"2" }),
            "qtt": TextInput(attrs={"type":"number", "class":"form-control", "name":"integerInput" ,"placeholder":"Ce champs doit être un entier" }),
            "destinationCompte": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "natureAchat": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "na_autre": TextInput(attrs={"class":"form-control","type":"text" , "placeholder":"veuillez spécifier la nature de l'achat"}),
            "miseDiso": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "md_autre": TextInput(attrs={"class":"form-control","type":"text" , "placeholder":"veuillez spécifier la mise à dispo"}),
            "affectationAchat": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
           
            
        }
        

