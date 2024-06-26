from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *



class Formulario_registro (forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class Formulario_musica (forms.Form):
    
    name_song = forms.CharField()
    artist = forms.CharField()
    gender = forms.CharField()
    release_year = forms.IntegerField()
    
class Formulario_artista(forms.Form):
    
    name = forms.CharField()
    country = forms.CharField()
    birthdate = forms.DateField()
    important_albums = forms.CharField()
    
class Formulario_instrumento(forms.Form):
    
    name = forms.CharField()
    brand = forms.CharField()
    model = forms.CharField()
    number_series = forms.IntegerField()

class UsereEditForm(UserChangeForm):
    
    password = forms.CharField(help_text="", widget=forms.HiddenInput(), required=False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="New password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden. Intentelo nuevamente.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
            if commit:
                user.save()
        return user

class FormularioAvatar (forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ('imagen',)


class BusquedaForm(forms.Form):
    marca = forms.CharField(label='Buscar instrumento por marca/modelo', max_length=100)
    







 