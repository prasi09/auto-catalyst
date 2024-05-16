from django.contrib import admin
from .models import car
# Register your models here.

@admin.register(car)
class Car_model_admin(admin.ModelAdmin):
    list_display=[
         'brand',    'car_type',    'car_model_name',    'transmission',    'fuel',    'model_year',
        'ownership',    'km_driven',    'price',    'location',    'chassis_no',    'registration_no',
        'photo_of_bluebook',    'feature_photo',    'gallery_1',    'gallery_2',    'gallery_3',
        'gallery_4',    'gallery_5',    'gallery_6',    'gallery_7',    'gallery_8',    'gallery_9',
        'gallery_10',    'description',    'mileage','id','date','contact_no'
    ] #,    'contact_no'
