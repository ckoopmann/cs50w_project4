from django.db import models

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

class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        display = f"{self.menuitem.id} - {self.menuitem.type}, {self.menuitem.name}, {self.menuitem.size} - Toppings: "

        for topping in self.toppings.all():
            display +=f" {topping.name},"

        return display
