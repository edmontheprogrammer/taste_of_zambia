from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "shawarma/home.html")


def order(request):
    return render(request, "shawarma/order.html")
