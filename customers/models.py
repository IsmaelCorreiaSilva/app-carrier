from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=8)
    number = models.CharField(max_length=5)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=80)

    def __str__(self):
        return self.name