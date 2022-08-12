from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserCreationFormWithEmail(UserCreationForm):
    
    email=forms.EmailField(required=True,
        help_text= "Requerido. 254 carácteres como máximo y debe ser un email válido.")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya esta registrado, prueba con otro.')
        
        return email