from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Aprendiz


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}))
    dependencia = forms.CharField(label="", max_length=45,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dependencia'}), disabled="True", initial="Teleinformática")
    rol_choices = [
    ('1', 'Administrador'),
    ('2', 'Instructor'),
    ('3', 'Aprendiz')]
    rol = forms.ChoiceField(label="", choices=rol_choices,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'dependencia','rol', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Documento de identidad'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Ingrese su documento de identidad sin letras ni caracteres especiales</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Su contraseña no puede ser muy similar a su otra información personal.</li><li>Su contraseña debe contener al menos 8 caracteres.</li><li>Su contraseña no puede ser una contraseña de uso común.</li><li>Su contraseña no puede ser completamente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme su contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña que antes, para verificación.</small></span>'

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    documento_aprendiz = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Documento aprendiz", "class": "form-control"}), label="")
    nombres_aprendiz = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombres aprendiz", "class": "form-control"}), label="")
    apellidos_aprendiz = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "Apellidos aprendiz", "class": "form-control"}),label="")
    correo_personal_aprendiz = forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "Correo personal", "class": "form-control"}),label="")
    correo_institucional_aprendiz = forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "Correo institucional", "class": "form-control"}),label="")
    # ficha_aprendiz = Aprendiz.ficha_aprendiz(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "Ficha", "class": "form-control"}),label="")
    celular_aprendiz = forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "Celular aprendiz", "class": "form-control"}),label="")
    # estado_asitencia_aprendiz = forms.BooleanField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "Estado asistencia", "class": "form-control"}),label="")
    class Meta:
        model = Aprendiz
        exclude = ("user",)
