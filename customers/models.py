from django.db import models
from django.urls import reverse

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=11) 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})
    
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    zip_code = models.CharField(max_length=10)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name="addresses")
    number = models.CharField(max_length=5)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.zip_code} - {self.street} - {self.district} - {self.city}"