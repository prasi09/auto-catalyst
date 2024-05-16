from django.urls import path,include
from . import views

app_name='contact'

urlpatterns = [
    path('', views.contact_view, name="contact"),
]
