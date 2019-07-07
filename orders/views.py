from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def index(request):

    types  = MenuItem.objects.order_by().values_list('type', flat = True).distinct()

    type_dict = {}

    for type in types:
        values = {}

        names = MenuItem.objects.filter(type = type).values_list('name', flat = True).distinct()

        for name in names:
            values[name] = MenuItem.objects.filter(type = type, name = name)

        type_dict[type] = values

    print(type_dict)

    context = {'types' : type_dict}

    return render(request, "orders/index.html", context)
