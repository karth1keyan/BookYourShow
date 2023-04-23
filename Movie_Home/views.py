from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def main(request):
    return render(request, 'Movie_Home/main.html')


def seats(request):
    return render(request, 'Movie_Home/seat.html')
