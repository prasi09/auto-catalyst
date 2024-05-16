from .models import contact
from django.views import View
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form= forms.contact_form(request.POST, request.FILES)
        name=request.POST['name']        
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        message=request.POST['message']
        values={
            'name':name,
            'email':email,
            'phone_no':phone_no,
            'message':message
        }
        if form.is_valid():
            form.save()
            messages.success(request,"Your contact form has been successfully submitted!")
            return redirect('/')
    else:
        form= forms.contact_form()  
        values={
            'name':'',
            'email':'',
            'phone_no':'',
            'message':''
        }
              
    return render(request, 'contact/contact.html',{ 'form': form })


