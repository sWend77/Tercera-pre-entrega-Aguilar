from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User 
from .models import *
from datetime import datetime


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

class CreditoForm(forms.Form):
    numero_de_tarjeta = forms.CharField(
        max_length=19,  
        min_length=13,  
        widget=forms.TextInput(attrs={'placeholder': '1234 5678 9012 3456'}),
        label="Número de Tarjeta",
        required=True
    )
    nombre_y_apellido = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del Titular'}),
        label="Nombre y Apellido del Titular",
        required=True
    )
    fecha_de_vencimiento = forms.DateField(
        label="Fecha de Vencimiento",
        input_formats=['%Y-%m'],  # Formato esperado por Django (AAAA-MM)
        widget=forms.DateInput(attrs={'placeholder': 'MM/AA', 'type': 'month'}),
        required=True
    )
    codigo_de_seguridad = forms.CharField(
        max_length=4,  
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'CVV'}),
        label="Código de Seguridad (CVV)",
        required=True
    )
    dni_del_titular = forms.CharField(
        max_length=10,  
        widget=forms.TextInput(attrs={'placeholder': 'DNI del Titular'}),
        label="DNI del Titular",
        required=True
    )

    def clean_numero_de_tarjeta(self):
        data = self.cleaned_data['numero_de_tarjeta']
        if not data.isdigit() or not (13 <= len(data.replace(' ', '')) <= 19):
            raise forms.ValidationError("Número de tarjeta no válido. Debe tener entre 13 y 19 dígitos.")
        return data.replace(' ', '')

    def clean_codigo_de_seguridad(self):
        data = self.cleaned_data['codigo_de_seguridad']
        if not data.isdigit() or not (3 <= len(data) <= 4):
            raise forms.ValidationError("Código de seguridad no válido. Debe tener 3 o 4 dígitos.")
        return data

    def clean_dni_del_titular(self):
        data = self.cleaned_data['dni_del_titular']
        if not data.isdigit():
            raise forms.ValidationError("DNI no válido. Debe contener solo números.")
        return data

    def clean_fecha_de_vencimiento(self):
        fecha_de_vencimiento = self.cleaned_data['fecha_de_vencimiento']
        if fecha_de_vencimiento:
            # Validar que la fecha sea mayor o igual a la fecha actual
            today = datetime.today().date()
            if fecha_de_vencimiento < today:
                raise forms.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")
        return fecha_de_vencimiento
 