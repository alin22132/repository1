from django.db import models

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    price_month = models.CharField(max_length=10, default='N/A')
    shorter_info = models.TextField(default='N/A')
    short_info = models.TextField(default='short info')
    traction = models.TextField(default='N/A')
    gearbox = models.TextField(default='Automatic')
    engine = models.TextField(default='N/A')
    stock = models.TextField(default='N/A')
    vin = models.TextField(default='N/A')
    mileage = models.TextField(default='N/A')
    body_color = models.TextField(default='N/A')
    interior_color = models.TextField(default='N/A')
    year = models.IntegerField()
    main_photo = models.ImageField(upload_to='taciki/', default='default_photo.jpg')

    def __str__(self):
        return f"{self.brand} {self.model} {self.type}({self.year}) {self.engine}"



class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='car_photos/')

# Create your models here.
