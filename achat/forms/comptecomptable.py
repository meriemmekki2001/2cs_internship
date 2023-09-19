from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Row, Fieldset, Submit, Field, ButtonHolder

from crispy_bootstrap5.bootstrap5 import FloatingField

from ..models import CompteComptable


class ComptecomptableForm(forms.ModelForm):
    class Meta:
        model = CompteComptable
        fields = ('code_comptable','nom_compte')
       




