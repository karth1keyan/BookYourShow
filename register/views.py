from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'register/index.html')

def location(request):
    return render(request,"register/loc.html")

def pay(request):
    return render(request, "register/pay.html")

def popup(request):
    return render(request, "register/pop.html")