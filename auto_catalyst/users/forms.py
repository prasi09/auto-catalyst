from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from users.models import MyUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('phone_no','email','name','address','password1','password2','prop_name','pan_no')
        
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        try:
            users=MyUser.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")
    
    def clean_phone(self):
        phone_no=self.cleaned_data['phone_no']
        try:
            users=MyUser.objects.get(phone_no=phone_no)
        except Exception as e:
            return phone_no
        raise forms.ValidationError(f"Phone number {phone_no} is already in use.")
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get("password1")
    #     password2 = cleaned_data.get("password2")

    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match.")

    #     return cleaned_data
    
    
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

    
class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
