from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth import authenticate

class SignupForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
        )
    class Meta:
        model=User       
        fields=['email','username','phonenumber','profile_img','password']
        
    def save(self,commit=True):
        user=super().save(commit=True)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        #exclude=["groups",'user_permissions','is_active','is_superuser','is_staff','is_guest','is_user','category','last_login']
        



class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data= super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email,password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password")
            self.user=user
        return cleaned_data