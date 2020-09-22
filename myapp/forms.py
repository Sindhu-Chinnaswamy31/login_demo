from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')