from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"[{self.no_of_guests}]{self.name} - {self.booking_date}"

    def __repr__(self):
        return f"Booking(name={self.name}, no_of_guests={self.no_of_guests}, booking_date={self.booking_date})"

    class Meta:
        ordering = ['name']

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.name} : {self.price}"

    class Meta:
        ordering = ['name']
