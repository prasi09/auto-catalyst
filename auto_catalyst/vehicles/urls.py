from django.urls import path
from . import views

app_name='vehicles'

urlpatterns = [
    # path('sell-car',views.Sell_car_view.as_view(), name="sell-car")
    path('sell-car',views.sellcar_view, name="sell-car"),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('c', views.cars, name='cars-view'),#not added
]
