from unicodedata import name
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from .validators import validate_date

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1)])
    booking_date = models.DateTimeField(validators=[validate_date])

    def __str__(self):
        return f'{self.name} | {self.booking_date.year}-{self.booking_date.month}-{self.booking_date.day} | {self.booking_date.hour}:{self.booking_date.minute}'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
