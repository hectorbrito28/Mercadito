from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from .models import Product,Mensaje


UserActual = get_user_model()

#Creando formularios

class MensajeForm(forms.ModelForm):
    to = forms.CharField(widget=forms.EmailInput,max_length=120)
    content = forms.CharField(widget=forms.Textarea,max_length=200)
    
    class Meta:
        model = Mensaje
        fields = ["to","content"]




class UserRegisterForm(UserCreationForm):
    dni = forms.CharField(widget=forms.NumberInput(),required=True,label="DNI")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput())
    class Meta:
        model = UserActual
        fields = ["username","dni","email","password1","password2"]
        
        #Remover textos de ayuda
        help_texts = {k:"" for k in fields}


#Subir prodcuto con foreigkey automatica
class UploadImageProduct(forms.ModelForm):
    
    
    class Meta:
        model = Product
        fields = ["productimage","name","description","price","category"]


class Product(forms.Form):
    name = forms.CharField(max_length=200,required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    price = forms.IntegerField(required=True)
    
    
    
    
        
    
    