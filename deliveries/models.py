from django.db import models
from customers.models import Customer

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    delivery_data = models.DateField(null=True)
    delivery_forcast = models.DateField(null=True)
    dimensions =  models.CharField(max_length=100)
    wieght = models.FloatField()
    amout = models.FloatField()

    def __str__(self):
        return self.model
    
class DeliveryRequest(models.Model):
    id = models.AutoField(primary_key=True)
    request_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='dr_customer')
    zip_code = models.CharField(max_length=8)
    number = models.CharField(max_length=5)
    height = models.FloatField()
    depth = models.FloatField()
    width = models.FloatField()
    wieght = models.FloatField()
    estimated_price = models.FloatField()

    def __str__(self):
        return self.request_date