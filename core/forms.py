from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect

elegir =(
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Prefiero_no_decirlo", "Prefiero no decirlo"),
    
)

class formularioRegistroUsuario(UserCreationForm):
   
        first_name = forms.CharField(label='Nombre')
        last_name = forms.CharField(label='Apellidos')
        # gender = forms.MultipleChoiceField(choices=elegir, label='Genero')
        username = forms.CharField(label='Nombre de usuario')
        email = forms.EmailField(label='Correo')
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
        
        class Meta:
                model = User
                fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
                help_texts = {k:"" for k in fields}

        first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
        # gender = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=elegir, )
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
        email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))