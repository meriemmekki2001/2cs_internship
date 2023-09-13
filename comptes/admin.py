from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User,Structure


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmation du mot de passe", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "first_name","last_name","departement"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "first_name","last_name","matricule", "password", "is_active",]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["email", "first_name","last_name","departement"]
    list_filter = ["email"]
    fieldsets = [
        (None, {"fields": ["email", "password","first_name","last_name"]}),
        ("Personal info", {"fields": ["profile_picture","departement","responsable","is_active"]}),
        ("Permissions", {"fields": ["is_staff","is_superuser"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name","last_name", "password1", "password2","departement","responsable"],
            },
        ),
    ]
    search_fields = ["email","first_name","last_name","matricule"]
    ordering = ["last_name"]
    filter_horizontal = []



admin.site.register(User, UserAdmin)


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin) :
    list_display = ['id' ,'nom']
    list_per_page = 10
    search_fields = ['nom__istartswith']
    ordering = ['nom']
    
