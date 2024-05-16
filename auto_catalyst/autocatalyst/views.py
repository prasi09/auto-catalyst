from django.shortcuts import render
from vehicles.models import car
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def homepage(request):
    cars = car.objects.order_by('-date')[:4]
    paginator = Paginator(cars, 4)
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
    return render(request,'home.html',data)


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')