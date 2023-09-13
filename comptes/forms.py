from django import forms
from django.contrib.auth import get_user_model



class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail",widget=forms.TextInput(attrs={"type":"email", "class": "form-control","placeholder":"Veuillez saisir votre e-mail "}))
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={"type":"password", "class": "form-control","placeholder":"Veuillez saisir votre mot de passe "}))
    