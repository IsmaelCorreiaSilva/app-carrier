from django import forms
from cars.models import Car, VehicleType, Brand

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class VehicleTypeModelForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'

class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
