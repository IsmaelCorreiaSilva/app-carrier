from django import forms
from customers.models import Customer, Address

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['zip_code', 'number', 'street', 'district', 'city', 'state']

    def __init__(self, *args, customer=None, **kwargs):
        super().__init__(*args, **kwargs)
        if customer:
             self.instance.customer = customer   