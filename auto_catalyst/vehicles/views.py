from .models import car
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from users.models import MyUser


# Create your views here.

#add redirect

# def pos(self, request):
#         form= forms.Car_form(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'vehicles/carSell.html', {'form':form})
def car_detail(request, id):
    single_car = get_object_or_404(car, pk=id)
    
    q1 = MyUser.objects.all().filter(id=single_car.contact_no.id).values()
    data = {
        'single_car': single_car,
        'q1':q1
    }
    return render(request, 'vehicles/car_detail.html', data)

def cars(request):
    cars = car.objects.order_by('-date')
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    car_model_name_search = car.objects.values_list('car_model_name', flat=True).distinct()
    location_search = car.objects.values_list('location', flat=True).distinct()
    model_year_search = car.objects.values_list('model_year', flat=True).distinct()
    car_type_search = car.objects.values_list('car_type', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'car_model_name_search': car_model_name_search,
        'location_search': location_search,
        'model_year_search': model_year_search,
        'car_type_search': car_type_search,
    }
    return render(request, 'vehicles/car_list_display.html' , data)
    

        

@login_required(login_url="/users/login/")
def sellcar_view(request):
    if request.method == 'POST':
        form= forms.Car_form(request.POST, request.FILES)
        if form.is_valid():
            newcar= form.save(commit=False)
            newcar.contact_no=request.user
            newcar.save()
            messages.success(request,"Your car has been successfully registered!")
            return redirect('vehicles:cars-view')
    else:
        form= forms.Car_form()  
              
    return render(request, 'vehicles/carSell.html',{ 'form': form })

