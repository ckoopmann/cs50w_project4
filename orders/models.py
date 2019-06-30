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
