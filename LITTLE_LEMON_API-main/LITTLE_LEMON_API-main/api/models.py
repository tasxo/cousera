from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=200)
    guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.date}"
