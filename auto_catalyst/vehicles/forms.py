from django import forms
from .models import car

Transmission_type = [
    ('Manual','Manual'),
    ('Automatic','Automatic')
]

Fuel_type=[
    ('Diesel','Diesel'),
    ('Petrol','Petrol'),
    ('Electric','Electric')
]
class Car_form(forms.ModelForm):
    transmission = forms.ChoiceField(choices=Transmission_type,widget=forms.RadioSelect(attrs={'class':'radio-button', 'input type':'radio' ,'id':'option1' ,'name':'Transmission_type', 'value':'Transmission'}),error_messages={'required':'Please choose your transmission type'})
    fuel = forms.ChoiceField(choices=Fuel_type,widget=forms.RadioSelect(attrs={'class':' active radio-button'}),error_messages={'required':'Please choose your car fuel type'} )
    class Meta:
        model = car
        fields = (
            'brand',        'car_model_name', 'car_type',      'model_year', 'transmission', 'fuel',
        'ownership',    'km_driven',    'price',    'location',    'chassis_no',    'registration_no',
            'mileage', 'photo_of_bluebook',    'feature_photo',    'gallery_1',    'gallery_2',    'gallery_3',
        'gallery_4',    'gallery_5',    'gallery_6',    'gallery_7',    'gallery_8',    'gallery_9',
        'gallery_10',    'description'
        )
        labels={
            'brand':'Car Brand', 'car_model_name':'Model Name',   'fuel':'Fuel Type',  'km_driven':'Kilometer Driven',
        'photo_of_bluebook':'Photo of Blue Book','chassis_no':'Chassis Number/Engine Number', 'gallery_1':'gallery',      'description':'Vehicle Description','gallery_2':'' ,    'gallery_3':'',
        'gallery_4':'',    'gallery_5':'',    'gallery_6':'',    'gallery_7':'',    'gallery_8':'',    'gallery_9':'',
        'gallery_10':''
        }
        error_messages={
            'brand':{'required':'Please select your car brand'},
            'car_model_name':{'required':'Please enter your car model'} ,       
            'car_type':{'required':'Please select your car type'} ,    
            'model_year':{'required':'Please enter your car model year'} ,       
            'ownership':{'required':'Please enter your car ownership status'} ,       
            'km_driven':{'required':'Please enter your km driven by your car'} ,       
            'price':{'required':'Please enter your the car price'} ,       
            'location':{'required':'Please enter location of your car'} ,       
            'chassis_no':{'required':'Please enter your car chassis/engine number'} ,
            'chassis_no':{'unique':'This Chassis/Engine number already exists.Please enter proper number.'} ,       
            'registration_no':{'required':'Please enter your car registration number'} ,       
            'registration_no':{'unique':'This Registration number already exists.Please enter proper number.'} ,
            'photo_of_bluebook':{'required':'Please upload blue book of car'} ,       
            'feature_photo':{'required':'Please upload feature photo of car'} ,       
            'gallery_1':{'required':'At least 4 photos of car is required'} ,       
            'gallery_2':{'required':'At least 4 photos of car is required'} ,       
            'gallery_3':{'required':'At least 4 photos of car is required'} ,       
            'gallery_4':{'required':'At least 4 photos of car is required'} ,       
                   
        }
        widgets= {
            'brand':forms.Select(attrs={'class':'form-control'}),
            'car_type':forms.Select(attrs={'class':'form-control'}),
            'car_model_name':forms.TextInput(attrs={'class':'form-control'}),
            'model_year':forms.NumberInput(attrs={'class':'form-control'}),
            'ownership':forms.Select(attrs={'class':'form-control'}),
            'km_driven':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'chassis_no':forms.TextInput(attrs={'class':'form-control'}),
            'registration_no':forms.TextInput(attrs={'class':'form-control'}),
            'mileage':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'gallery_1':forms.ClearableFileInput(attrs={'class':'img','placeholder':'img'})
        }
    def clean(self):
        cleaned_data=super().clean()
        chassis_no=cleaned_data.get('chassis_no')
        description=cleaned_data.get('description')
        
        if chassis_no and len(chassis_no)<5:
            self.add_error('chassis_no','Chassis/Engine number should be at least 5 character long')

        if description and len(description)<12:
            self.add_error('description','Please enter a longer description of your car')

