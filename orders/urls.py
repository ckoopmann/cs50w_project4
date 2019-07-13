from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path("remove/<int:id>", views.remove, name="remove"),
    path("add/<int:id>", views.add, name="add")
]
