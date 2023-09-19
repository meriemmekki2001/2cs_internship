from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Row, Fieldset, Submit, Field, ButtonHolder
from django.urls import reverse
from django import forms
from ..models import Project,CompteComptableDetails



class ProjetForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('code_projet','nom_projet','chef_projet','sponsor','compte_comptable_detail')
      
    def __init__(self,*args, **kwargs):

        super(ProjetForm,self).__init__(*args, **kwargs)

        self.fields['chef_projet'].empty_label = "Select"
        self.fields['sponsor'].empty_label = "Select"
        self.fields['compte_comptable_detail'].queryset = CompteComptableDetails.objects.filter(status='Actif')
        self.fields['compte_comptable_detail'].required = False






