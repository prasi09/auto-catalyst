from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from users.forms import CustomUserCreationForm
from .forms import SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes ,force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from django.db.models.query_utils import Q



def register_view(request,*args,**kwargs):
    user=request.user
    if request.user.is_authenticated:
        return redirect('/')
    context={}

    if request.POST:
        form=CustomUserCreationForm(request.POST, request.FILES)
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        values={
            'name':name,
            'address':address,
            'email':email,
            'phone_no':phone_no,
        }
        if form.is_valid():
            user=form.save(commit= False)
            user.is_active= False
            user.user_type='user'
            user.save()
            
            
            current_site=get_current_site(request)
            mail_subject="Activate your account"
            message=render_to_string("users/account_activation_email.html",{
                "user":user,
                "domain":current_site.domain,
                "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                "token":account_activation_token.make_token(user),
                
            })
            # print(user.pk)
            to_email= form.cleaned_data.get("email")
            email=EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, "Please check your email to complete the registration.")
            return redirect('/')
    else:
        form=CustomUserCreationForm()
        values={
            'name':'',
            'address':'',
            'email':'',
            'phone_no':'',
        }
        
    context={
        'registration_form':form,
        'values':values,
    }
    return render(request,'users/register.html',context)

def agent_register_view(request,*args,**kwargs):
    user=request.user
    if request.user.is_authenticated:
        return redirect('/')
    context={}

    if request.POST:
        form=CustomUserCreationForm(request.POST, request.FILES)
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        values={
            'name':name,
            'address':address,
            'email':email,
            'phone_no':phone_no,
        }
        if form.is_valid():
            user=form.save(commit= False)
            user.is_active= False
            user.user_type='agent'
            user.save()
            
            
            current_site=get_current_site(request)
            mail_subject="Activate your account"
            message=render_to_string("users/account_activation_email.html",{
                "user":user,
                "domain":current_site.domain,
                "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                "token":account_activation_token.make_token(user),
                
            })
            # print(user.pk)
            to_email= form.cleaned_data.get("email")
            email=EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, "Please check your email to complete the registration.")
            return redirect('/')
    else:
        form=CustomUserCreationForm()
        values={
            'name':'',
            'address':'',
            'email':'',
            'phone_no':'',
        }
        
    context={
        'registration_form':form,
        'values':values,
    }
    return render(request,'users/agent_register.html',context)


def activate(request, uidb64, token):
    MyUser= get_user_model()
    
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user= MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user=None
        
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        # user.is_confirmed=True
        user.save()
        
        # login(request,user)
        
        messages.success(request,"Your account has been successfully activated!")
        return redirect(reverse('users:login'))
    
    else:
        messages.error(request,"Activation link is in valid or expired.")
        return redirect('/')
        

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        phone_no= request.POST['phone_no']
        password= request.POST['password']
        
        user= authenticate(request,username=phone_no,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged-In")
            if "next" in request.GET:
                return redirect(request.GET.get("next"))
            else:
                return redirect('/')
        
        else:
            messages.error(request,"Username or Password doesn't match the credentials")
            return redirect('users:login')
    
    return render(request,'users/login.html')
    # return render(request, "users/login.html", { "form": form })

def logout_view(request):
    logout(request)
    messages.success(request,"Successfully Logged-Out")
    return redirect('/')
    
        
@login_required(login_url="/users/login/")
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('users:login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'users/password_reset_confirm.html', {'form': form})

@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form=PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("users/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        "Password reset request has been sent! Please check your register email."
                    )
                else:
                    messages.error(request, "Problem sending reset password email, SERVER PROBLEM")
            else:
                messages.error(request, "The email doesn't match your credentials.")
            return redirect('/')

        # for key, error in list(form.errors.items()):
        #     if key == 'captcha' and error[0] == 'This field is required.':
        #         messages.error(request, "You must pass the reCAPTCHA test")
        #         continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="users/password_reset.html", 
        context={"form": form}
        )
    
def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and log in now.")
                return redirect('/')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'users/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("/")

        
        
        
        
        
        
        
        
        
        
        
        

   # if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
          #  login(request, user)
           # return redirect('home')
        # else:
          #  error_message = 'Invalid username or password.'
           # return render(request, 'login.html', {'error_message': error_message})
           
# Create your views here.
# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         email=request.POST['email']
#         phone_no=request.POST['phone_no']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
       
#         phone_no_check=User.objects.filter(username=phone_no).exists()
#         if phone_no_check == True:
#             messages.error(request,"The phone number is already used!!")
#             return redirect('users:register',{'value':value})
        
#         email_check=User.objects.filter(email=email).exists()
#         if email_check == True:
#             messages.error(request,"The email is already used!!")
#             return redirect('users:register',{'value':value})
        
#         if len(phone_no)!=10:
#             messages.error(request,'Number Should be 10 Digit')
#             # messages.add_message(request, messages.INFO, "Hello world.")
#             return redirect('users:register',{'value':value})
        
#         elif password1 != password2:
#             messages.error(request,"Password and confirm password didn't match")
#             return redirect('users:register',{'value':value})
        
#         else:
#             user=User.objects.create_user(username=phone_no,email=email,password=password1)
#             user.first_name=fname
#             user.last_name=lname
#             user.save()
#             messages.success(request,"Your account Successfully Created")
#             return redirect('users:login')

    #     phone_no_check = MyUser.objects.filter(username=phone_no).exists()
    #     if phone_no_check:
    #         messages.error(request, "The phone number is already used!!")
    #         return render(request, "users/register.html", {'value': value})

    #     email_check = User.objects.filter(email=email).exists()
    #     if email_check:
    #         messages.error(request, "The email is already used!!")
    #         return render(request, "users/register.html", {'value': value})

    #     if len(phone_no) != 10:
    #         messages.error(request, 'Number Should be 10 Digit')
    #         return render(request, "users/register.html", {'value': value})

    #     if password1 != password2:
    #         messages.error(request, "Password and confirm password didn't match")
    #         return render(request, "users/register.html", {'value': value})
        
    #     else:
    #         user = MyUser.objects.create_user(username=phone_no, email=email, password=password1)
    #         user.first_name = fname
    #         user.last_name = lname
    #         user.save()
    #         messages.success(request, "Your account Successfully Created")
    #         return redirect('users:login')

    # return render(request, "users/register.html")
        
    
    # return render(request, "users/register.html")