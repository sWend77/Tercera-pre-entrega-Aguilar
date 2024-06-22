from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
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

class UsereEditForm (UserChangeForm):
    
    password = forms.CharField(help_text="", widget = forms.HiddenInput(), required= False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


























 