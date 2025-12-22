from django.db import models

# Create your models here.
class MenuTable(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} : {self.price}"
    
class BookingTable(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"