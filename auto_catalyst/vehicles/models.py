from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from users.models import MyUser

# Create your models here.

CAR_MANUFACTURERS = [
    ('Acura', 'Acura'),
    ('Alfa Romeo', 'Alfa Romeo'),
    ('Alpine', 'Alpine'),
    ('Arash', 'Arash'),
    ('Ariel', 'Ariel'),
    ('Artega', 'Artega'),
    ('Ascari', 'Ascari'),
    ('Aston Martin', 'Aston Martin'),
    ('Audi', 'Audi'),
    ('AvtoVAZ', 'AvtoVAZ'),
    ('Bentley', 'Bentley'),
    ('BMW', 'BMW'),
    ('Bufori', 'Bufori'),
    ('Bugatti', 'Bugatti'),
    ('Buick', 'Buick'),
    ('Byton', 'Byton'),
    ('Cadillac', 'Cadillac'),
    ('Chery', 'Chery'),
    ('Chevrolet', 'Chevrolet'),
    ('Chrysler', 'Chrysler'),
    ('CT&T', 'CT&T'),
    ('Dacia', 'Dacia'),
    ('Daewoo', 'Daewoo'),
    ('DAF', 'DAF'),
    ('Datsun', 'Datsun'),
    ('Dodge', 'Dodge'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Fisker', 'Fisker'),
    ('Force Motors', 'Force Motors'),
    ('Ford', 'Ford'),
    ('Foton', 'Foton'),
    ('GAZ', 'GAZ'),
    ('Geely', 'Geely'),
    ('Genesis', 'Genesis'),
    ('Ginetta', 'Ginetta'),
    ('GMC', 'GMC'),
    ('Honda', 'Honda'),
    ('Hyundai', 'Hyundai'),
    ('Iconic', 'Iconic'),
    ('Infiniti', 'Infiniti'),
    ('Isuzu', 'Isuzu'),
    ('JAC', 'JAC'),
    ('Jaguar', 'Jaguar'),
    ('Jeep', 'Jeep'),
    ('JMC', 'JMC'),
    ('Kia', 'Kia'),
    ('Koenigsegg', 'Koenigsegg'),
    ('Lamborghini', 'Lamborghini'),
    ('Lancia', 'Lancia'),
    ('Land Rover', 'Land Rover'),
    ('Landwind', 'Landwind'),
    ('Lexus', 'Lexus'),
    ('Lotus', 'Lotus'),
    ('Luxgen', 'Luxgen'),
    ('Magna Steyr', 'Magna Steyr'),
    ('Mahindra', 'Mahindra'),
    ('Maserati', 'Maserati'),
    ('Maxus', 'Maxus'),
    ('Maybach', 'Maybach'),
    ('Mazda', 'Mazda'),
    ('Mazzanti', 'Mazzanti'),
    ('McLaren', 'McLaren'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('MG', 'MG'),
    ('Mini', 'Mini'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Mitsuoka', 'Mitsuoka'),
    ('Nissan', 'Nissan'),
    ('Pagani', 'Pagani'),
    ('Perodua', 'Perodua'),
    ('Peugeot', 'Peugeot'),
    ('Pontiac', 'Pontiac'),
    ('Porsche', 'Porsche'),
    ('Proton', 'Proton'),
    ('Reliant', 'Reliant'),
    ('Renault', 'Renault'),
    ('Rolls-Royce', 'Rolls-Royce'),
    ('RUF', 'RUF'),
    ('Saab', 'Saab'),
    ('Saleen', 'Saleen'),
    ('Saturn', 'Saturn'),
    ('Scion', 'Scion'),
    ('SEAT', 'SEAT'),
    ('Skoda', 'Skoda'),
    ('Spyker', 'Spyker'),
    ('Ssangyong', 'Ssangyong'),
    ('Subaru', 'Subaru'),
    ('Suzuki', 'Suzuki'),
    ('Tata', 'Tata'),
    ('Tatra', 'Tatra'),
    ('Tesla', 'Tesla'),
    ('Toyota', 'Toyota'),
    ('Trumpchi', 'Trumpchi'),
    ('TVR', 'TVR'),
    ('Vauxhall', 'Vauxhall'),
    ('Volkswagen', 'Volkswagen'),
    ('Volvo', 'Volvo'),
    ('W Motors', 'W Motors'),
    ('Wiesmann', 'Wiesmann'),
    ('Zenos', 'Zenos'),
    ('Zenvo', 'Zenvo'),
]

CAR_TYPES = [
    ('Sedan', 'Sedan'),
    ('SUV', 'SUV'),
    ('Pick-up', 'Pick-up'),
    ('CUV/XUV', 'CUV/XUV'),
    ('MUV', 'MUV'),
    ('Electric', 'Electric'),
    ('Hatchback', 'Hatchback'),
    ('Van', 'Van'),
    ('Sports', 'Sports'),
    ('Convertible', 'Convertible'),
    ('Luxury', 'Luxury'),
]

Transmission_type = [
    ('Manual','Manual'),
    ('Automatic','Automatic'),
]

Fuel_type=[
    ('Diesel','Diesel'),
    ('Petrol','Petrol'),
    ('Electric','Electric'),
]

Owner_type=[
    ('1st owner','1st owner'),
    ('2nd owner','2nd owner'),
    ('3rd owner','3rd owner'),
    ('4th owner','4th owner'),
    ('5th owner','5th owner'),
]

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(choices=CAR_MANUFACTURERS ,max_length=50)
    car_type = models.CharField(choices=CAR_TYPES ,max_length=50)
    car_model_name = models.CharField(max_length=70)
    transmission =  models.CharField(max_length=12,choices=Transmission_type,null=False,blank=False)
    fuel = models.CharField(max_length=12,choices=Fuel_type,null=False,blank=False)
    model_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1980), max_value_current_year])
    ownership = models.CharField(choices=Owner_type ,max_length=12)
    km_driven =  models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    chassis_no = models.CharField(max_length=20,unique=True)
    registration_no = models.CharField(max_length=20, unique=True)
    photo_of_bluebook = models.ImageField( upload_to='images/bluebook')
    feature_photo = models.ImageField( upload_to='images/feature')
    gallery_1 = models.ImageField(upload_to='images/gallery')
    gallery_2 = models.ImageField(upload_to='images/gallery')
    gallery_3 = models.ImageField(upload_to='images/gallery')
    gallery_4 = models.ImageField(upload_to='images/gallery')
    gallery_5 = models.ImageField(upload_to='images/gallery',blank=True)
    gallery_6 = models.ImageField(upload_to='images/gallery',blank=True)
    gallery_7 = models.ImageField(upload_to='images/gallery',blank=True)
    gallery_8 = models.ImageField(upload_to='images/gallery',blank=True)
    gallery_9 = models.ImageField(upload_to='images/gallery',blank=True)
    gallery_10 = models.ImageField(upload_to='images/gallery',blank=True)
    description = models.TextField()
    mileage =models.SmallIntegerField(blank=True,null=True)
    date= models.DateTimeField(auto_now_add=True)
    contact_no =models.ForeignKey(MyUser, on_delete=models.CASCADE,default=None) 

    def __str__(self):
        return self.brand