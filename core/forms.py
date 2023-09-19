from django import forms
from django.forms import inlineformset_factory
from .models import PreDemande, Produit,Categorie,Fournisseur
from django.forms import ModelForm, Textarea,Select,TextInput
from django.utils.translation import gettext_lazy as _


class PreDemandeForm(forms.ModelForm):
    class Meta:
        model = PreDemande
        fields = ["destinationCompte","natureAchat","na_autre","miseDiso","md_autre","affectationAchat"]
        widgets = {
            "destinationCompte": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "natureAchat": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "na_autre": TextInput(attrs={"class":"form-control","type":"text" , "placeholder":"veuillez spécifier la nature de l'achat"}),
            "miseDiso": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
            "md_autre": TextInput(attrs={"class":"form-control","type":"text" , "placeholder":"veuillez spécifier la mise à dispo"}),
            "affectationAchat": Select(attrs={"class":"form-control","aria-label":"Default select example" }),
           
            
        }
        labels = {
            "na_autre": _(""),
            "md_autre": _(""),
        }


class ProduitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["designation"]="test"
    class Meta:
        model = Produit
        fields = ["designation","qtt"]
        widgets = {
            "designation": TextInput(attrs={"class":"form-control","type":"text"}),
            "qtt": TextInput(attrs={"type":"number", "class":"form-control", "name":"integerInput" ,"placeholder":"Ce champs doit être un entier" }),}

ProduitFormSet = inlineformset_factory(PreDemande, Produit, form=ProduitForm, can_delete=False)


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ["matricule","nom","email","telephone","categorie"]
        widgets = {
            "matricule": TextInput(attrs={"class":"form-control","type":"text" }),
            "nom": TextInput(attrs={"class":"form-control","type":"text" }),
            "email": TextInput(attrs={"class":"form-control","type":"email" }),
            "telephone":TextInput(attrs={"class":"form-control","type":"tel" }),
            "categorie":Select(attrs={"class":"form-control","aria-label":"Default select example" }),
           
            
        }


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ["nom"]
        widgets = {
            "nom": TextInput(attrs={"class":"form-control","type":"text" }),}






