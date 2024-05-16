from django.contrib import admin
from .models import contact
# Register your models here.

@admin.register(contact)
class contact_admin(admin.ModelAdmin):
    list_display=[
            'name','email','phone_no','message'
    ]
