from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta :
        model = CustomUser
        fields = ['email','age','name','date_of_birth','phone_number','password1','password2']
    
class CustomUserChangeForm(UserChangeForm):
    class Meta :
        model = CustomUser
        fields = ['email','age','name','date_of_birth','phone_number']