from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Aprendiz


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}))
    dependencia = forms.CharField(label="", max_length=45,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dependencia'}), disabled="True", initial="Teleinformática")

    class Meta:
        model = User
        fields = ('username', 'dependencia', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Documento de identidad'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme su contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

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
