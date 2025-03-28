from django.db.models.signals import pre_save
from django.dispatch import receiver
from deliveries.models import DeliveryRequest
from datetime import date

@receiver(pre_save, sender=DeliveryRequest)
def delivery_request_pre_save(sender, instance, **kwargs):
    instance.request_date = date.today()
    instance.estimated_price = 2