from django import forms
from deliveries.models import DeliveryRequest

class DeliveryRequestModelForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = '__all__'
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date'})
        }