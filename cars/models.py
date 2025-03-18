from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class VehicleType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.CharField(max_length=4)
    model_year = models.CharField(max_length=4)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT, related_name='car_vehicle')
    
    def __str__(self):
        return self.model
