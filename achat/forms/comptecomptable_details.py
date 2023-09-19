from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Row, Fieldset, Submit, Field, ButtonHolder
from django import forms
from django.urls import reverse

from ..models import CompteComptableDetails



class ComptecomptableDetailForm(forms.ModelForm):

    class Meta:
        model = CompteComptableDetails
        fields = ('code_detail','budget','destination_achat_compte','devise','structure')
     

    def __init__(self,*args, **kwargs):
        super(ComptecomptableDetailForm,self).__init__(*args, **kwargs)
        self.fields['structure'].empty_label = "Select"
        self.fields['devise'].empty_label = "Select"
        self.fields['destination_achat_compte'].empty_label = "Select"
        self.fields['structure'].required = False



class ComptecomptableDetailFormDelete(forms.Form):

    class Meta:
        model = CompteComptableDetails
        

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            
                HTML(f'<p>Voulez vous supprimer ce compte detail</p>'),
            ButtonHolder(
                Submit('submit', 'Confirmer '),
            )
        )  