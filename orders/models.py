from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length = 30)
    size = models.CharField(max_length = 10)
    type = models.CharField(max_length = 30)
    prize = models.FloatField()
    num_toppings = models.IntegerField()


    def __str__(self):
        return f"{self.id} - {self.type}, {self.name}, {self.size}, {self.prize}"

class Topping(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Order(models.Model):
    status = models.CharField(max_length = 30, default = 'Open')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.status} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        display = f"{self.id} - {self.menuitem.type}, {self.menuitem.name}, {self.menuitem.size} - Quantity: {self.quantity} - Unit Prize: {self.menuitem.prize} - Toppings: "

        for topping in self.toppings.all():
            display +=f" {topping.name},"

        return display
