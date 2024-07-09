from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
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
    
class FormularioArtista(forms.Form):
    
    nombre_de_artista = forms.CharField(required=False)
    pais = forms.CharField(required=False)
    
    
    
class Formulario_instrumento(forms.Form):
    
    name = forms.CharField()
    brand = forms.CharField()
    model = forms.CharField()
    number_series = forms.IntegerField()

class UsereEditForm(UserChangeForm):
    password = forms.CharField(help_text="", widget=forms.HiddenInput(), required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput, required=False)
    direccion = forms.CharField(label="Dirección", max_length=255, required=False)
    piso = forms.IntegerField(label="Piso", required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "direccion", "piso"]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden. Inténtelo nuevamente.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)

        if commit:
            user.save()

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.direccion = self.cleaned_data['direccion']
        user_profile.piso = self.cleaned_data['piso']
        user_profile.save()

        return user

class FormularioAvatar (forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ['imagen']


class BusquedaForm(forms.Form):
    buscar = forms.CharField(label='Buscar instrumento por tipo, marca y/o modelo:', max_length=100)
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




 