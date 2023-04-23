from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="register_login"),
    path('loc/', views.location, name="register_location"),
    path('payment/', views.pay, name="Payment"),
    path('pop/', views.popup, name="Comfirmation"),
]
