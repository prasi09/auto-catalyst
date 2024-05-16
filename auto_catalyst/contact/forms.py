from django import forms
from .models import contact
from django_recaptcha.fields import ReCaptchaField

class contact_form(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model=contact
        fields =(
            'name','email','phone_no','message','captcha'
        )

        error_messages={
            'name':{'required':'Please enter your name'} ,
            'email':{'required':'Please enter your car email'} ,            
            # 'email':{'unique':'A contact form has already been filled by this email'},
            'phone_no':{'required':'Please enter your contact number'} ,
            # 'phone_no':{'unique':'A contact form has already been filled by this contact number'},
            'message':{'required':'Please enter your message'},
            'captcha':{'required':'Please enter the captcha'}
        }
        label={
             'captcha':''
        }

        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'})
        }

    def clean(self):
            cleaned_data=super().clean()
            message=cleaned_data.get('message')
            phone_no=cleaned_data.get('phone_no')

            if message and len(message)<20:
                self.add_error('message','Please enter a longer message')

            if phone_no and len(phone_no)!=10:
                self.add_error('phone_no','Please enter 10 digits in phone number')    