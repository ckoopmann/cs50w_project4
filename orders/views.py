from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MenuItem, OrderItem, Order
from .forms import OrderItemForm

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

    context = {'types' : type_dict}

    return render(request, "orders/index.html", context)


def add(request, id):
    menuitem = MenuItem.objects.get(pk = id)

    order = Order.objects.filter(user = request.user, status = 'Open').first()

    if order is None:
        order = Order(user = request.user, status = 'Open')
        order.save()

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderItemForm(initial = {'menuitem' : menuitem, 'order':order})
    context = {'menuitem' : menuitem,
    'form':form}

    return render(request, "orders/add.html", context)

def remove(request, id):
    OrderItem.objects.get(id=id).delete()
    return redirect('cart')

def cart(request):
    order = Order.objects.filter(user = request.user, status = 'Open').first()

    if order is None:
        order = Order(user = request.user, status = 'Open')
        order.save()

    orderitems = order.orderitem_set.all()
    context = {'order' : order, 'orderitems':orderitems}
    return render(request, "orders/cart.html", context)
