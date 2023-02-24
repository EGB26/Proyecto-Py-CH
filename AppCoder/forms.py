from django import forms
from .views import UserCreationForm
#from .forms import User
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
            #saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}