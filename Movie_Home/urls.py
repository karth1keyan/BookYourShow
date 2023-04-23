from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="Home page"),
    path('seats/', views.seats, name="seat booking")
]
