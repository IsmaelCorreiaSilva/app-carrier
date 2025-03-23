from django import forms
from cars.models import Car, VehicleType, Brand

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factory_year': 'Ano de Fabricação',
            'model_year': 'Ano do Modelo',
            'vehicle_type': 'Tipo do Veículo'
        }

class VehicleTypeModelForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name']
        labels = {
            'name': 'Nome'
        }

class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        labels = {
            'name': 'Nome'
        }
