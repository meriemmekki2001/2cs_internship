from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Row, Fieldset, Submit, Field, ButtonHolder
from django import forms
from django.urls import reverse
from django.forms import HiddenInput, TextInput

from ..models import DemandeAchat,Project,CompteComptable,CompteComptableDetails



class DemandeAchatForm(forms.ModelForm):
    designations=forms.CharField(widget=HiddenInput)
    fournisseurs=forms.CharField(widget=HiddenInput)
    prices=forms.CharField(widget=HiddenInput)
    qtys=forms.CharField(widget=HiddenInput)
    autre_mise_dispo = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '70'}))
    autre_affectation_achat = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '70'}))
    class Meta:
        model = DemandeAchat
        fields = ('destination_achat','nature_achat','autre_nature_achat','mise_dispo','autre_mise_dispo','affectation_achat','autre_affectation_achat','disponibilité','devise','code_comptable','code_comptable_detail')
      
       
        
    def __init__(self,*args, **kwargs):
        super(DemandeAchatForm,self).__init__(*args, **kwargs)
        self.fields['code_comptable_detail'].queryset = CompteComptableDetails.objects.none()
        self.fields['code_comptable'].queryset = CompteComptable.objects.none()

        
        
       # if ('code_comptable' in self.data and 'devise' in self.data and 'nature_achat' in self.data):
        if 'code_comptable' in self.data :
            try:
                code_comptable_id=int(self.data.get('code_comptable'))
                devise_id = self.data.get('devise')
                nature_achat_id = self.data.get('nature_achat')

                self.fields['code_comptable_detail'].queryset=CompteComptableDetails.objects.filter(code_comptable=code_comptable_id,devise=devise_id,destination_achat_compte=nature_achat_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            pass
          

        self.fields['destination_achat'].empty_label = "Select"
        self.fields['code_comptable'].empty_label = "Select"
        self.fields['code_comptable_detail'].empty_label = "Select"
        self.fields['nature_achat'].empty_label = "Select"

        self.fields['mise_dispo'].empty_label = "Select"
        self.fields['devise'].empty_label = "Select"
        self.fields['affectation_achat'].empty_label = "Select"
        self.fields['disponibilité'].empty_label = "Select"
        self.fields['nature_achat'].required = False
        self.fields['mise_dispo'].required = False
        self.fields['affectation_achat'].required = False
        self.fields['disponibilité'].required = True
        self.fields['autre_nature_achat'].required = False
        self.fields['autre_mise_dispo'].required = False
        self.fields['autre_affectation_achat'].required = False
        




