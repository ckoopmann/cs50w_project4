from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def index(request):
    context = {
    "regular_pizzas": MenuItem.objects.filter(type = "Regular Pizza"),
    "sicilian_pizzas": MenuItem.objects.filter(type = "Sicilian Pizza")
    }
    return render(request, "orders/index.html", context)
