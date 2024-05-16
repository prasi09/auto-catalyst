from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, phone_no, email, name, password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        if not name:
            raise ValueError("name is required")
        
        if not phone_no:
            raise ValueError("Phone number is required")
        
        user=self.model(
            phone_no=phone_no,
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone_no,name,email,password=None,**extra_fields):
        user=self.create_user(
            phone_no=phone_no,
            name=name,
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff=True
        user.is_superuser=True
        user.is_staff=True
        
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(verbose_name="email address",max_length=60,unique=True)
    phone_no=models.CharField(verbose_name="phone number",max_length=10,unique=True)
    name=models.CharField(verbose_name="Name",max_length=50)
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('agent', 'Agent'),
    )
    user_type = models.CharField( default='',max_length=50, null=False, blank=False, choices=USER_TYPE_CHOICES)
    is_confirmed = models.BooleanField(default=False)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    address=models.CharField(verbose_name="Address",max_length=80)
    pan_no=models.CharField(verbose_name="pan number",max_length=30,null=True,blank=True,unique=True)
    prop_name=models.CharField(verbose_name="Propritor Name",null=True,blank=True,max_length=80)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    
    USERNAME_FIELD="phone_no"
    
    REQUIRED_FIELDS=['email','name']
    
    objects=MyUserManager()
    
    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perm(self, app_label):
        return True
    