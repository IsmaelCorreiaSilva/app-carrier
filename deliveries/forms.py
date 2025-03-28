from django import forms
from deliveries.models import DeliveryRequest

class DeliveryRequestModelForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['pickup_schedule', 'zip_code', 'number', 'street', 'district', 'city', 'state', 'height', 'depth', 'width', 'wieght']
        labels = {
            
            'pickup_schedule': 'Dia de Retirada',
            'zip_code': 'CEP',
            'number': 'Número',
            'street': 'Rua',
            'district': 'Bairro',
            'city': 'Cidade',
            'state': 'Estado',
            'height': 'Altura',
            'depth': 'Profundidade',
            'width': 'Largura',
            'wieght': 'Peso',
        }
        widgets = {
            'pickup_schedule': forms.DateInput(attrs={'type': 'date'})
        }