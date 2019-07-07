from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def index(request):

    types  = MenuItem.objects.order_by().values_list('type', flat = True).distinct()

    context = {}

    for type in types:
        values = {}

        names = MenuItem.objects.filter(type = type).values_list('name', flat = True).distinct()

        for name in names:
            values[name] = MenuItem.objects.filter(type = type, name = name)

        context[type.replace(" ", "")+'s'] = values

    print(context)

    return render(request, "orders/index.html", context)
