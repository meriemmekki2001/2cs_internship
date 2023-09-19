from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Row, Fieldset, Submit, Field, ButtonHolder

from crispy_bootstrap5.bootstrap5 import FloatingField

from ..models import CompteComptable,ProductPurchase


class ProductPurchaseForm(forms.ModelForm):
    class Meta:
        model = ProductPurchase
        fields = ('designation','quantite','fournisseur','price')
       



    def __init__(self, *args, **kwargs):
        super(ProductPurchaseForm, self).__init__(*args, **kwargs)

