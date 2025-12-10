from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    number_plate = models.CharField()
    vehicle_type = models.CharField()
    manufacturer = models.CharField()
    year = models.IntegerField()

    def __str__(self):
        return self.number_plate

