from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Row, Fieldset, Submit, Field, ButtonHolder

from crispy_bootstrap5.bootstrap5 import FloatingField
from django.forms import HiddenInput, TextInput
from ..models import DemandePaiment


class DemandePaimentForm(forms.ModelForm):
    montant_chiffre = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    montant_lettres = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    devise = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    Num_compte = forms.CharField(required=False,widget=forms.TextInput(attrs={'defaultValue': ''}))
    rib = forms.CharField(required=False,widget=forms.TextInput(attrs={'defaultValue': ''}))
    adresse = forms.CharField(required=False,widget=forms.TextInput(attrs={'defaultValue': ''}))
    swift = forms.CharField(required=False,widget=forms.TextInput(attrs={'defaultValue': '',}))
    Num_fournisseur = forms.ChoiceField()
    beneficiaire = forms.CharField(required=False,widget=forms.TextInput(attrs={'defaultValue': '',}))
    bon_commande=forms.ChoiceField()
    num_facture=forms.CharField(required=False,widget=forms.TextInput(attrs={'defaultValue': '',}))
    
     

    class Meta:
        model = DemandePaiment
        fields = ('montant_chiffre','montant_lettres','mode_paiment','devise','Num_compte','rib','adresse','swift','objet_paiment','Num_fournisseur','beneficiaire','bon_commande','num_facture')
       




