from typing import Any
from django import forms
from customers.models import Customer, Address

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']
        labels = {
            'name': 'Nome',
            'phone': 'Telefone'
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')

            if len(name) < 4:
                raise forms.ValidationError('O campo Nome deve conter pelo mais 4 dígito!')
            
            if len(name) > 100:
                raise forms.ValidationError('O campo Nome deve conter no máximo 100 dígitos')
            
            return name
        
        def clean_email(self):
            email = self.cleaned_data.get('email')

            if len(email) < 4:
                raise forms.ValidationError('O campo Email deve conter pelo mais 4 dígito!')
            
            if len(email) > 100:
                raise forms.ValidationError('O campo Email deve conter no máximo 100 dígitos')
            
            return email
        
        def clean_phone(self):
            phone = self.cleaned_data.get('phone')

            if len(phone) < 8:
                raise forms.ValidationError('O campo Telefone deve conter pelo mais 4 dígito!')
            
            if len(phone) > 11:
                raise forms.ValidationError('O campo Telefone deve conter no máximo 11 dígitos')
            
            return phone

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['zip_code', 'number', 'street', 'district', 'city', 'state']
        labels = {
            'zip_code': 'CEP',
            'number':'Número',
            'street':'Rua',
            'district':'Bairro',
            'city': 'Cidade',
            'state': 'UF'
        }

    def __init__(self, *args, customer=None, **kwargs):
        super().__init__(*args, **kwargs)
        if customer:
             self.instance.customer = customer   

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')

        if len(zip_code) != 10:
            raise forms.ValidationError('O campo CEP deve conter 8 caracteres!')
        
        return zip_code
    
    def clean_number(self):
        number = self.cleaned_data.get('number')

        if len(number) < 1:
            raise forms.ValidationError('O campo Número deve conter pelo mais 1 dígito!')
        
        if len(number) > 6:
            raise forms.ValidationError('O campo Número deve conter no máximo 5 dígitos')
        
        return number
        
    def clean_street(self):
        street = self.cleaned_data.get('street')

        if len(street) < 4:
            raise forms.ValidationError('O campo Rua deve conter pelo mais 4 caracteres!')

        if len(street) > 100:
            raise forms.ValidationError('O campo Rua deve conter no máximo 100 caracteres!')
        
        return street
    
    def clean_distrist(self):
        district = self.cleaned_data.get('street')
        
        if len(district) < 4:
            raise forms.ValidationError('O campo Bairro deve conter pelo mais 4 caracteres!')

        if len(district) > 100:
            raise forms.ValidationError('O campo Bairro deve conter no máximo 100 caracteres!')
        
        return district

        
    def clean_city(self):
        city = self.cleaned_data.get('city')

        if len(city) < 4:
            raise forms.ValidationError('O campo Cidade deve conter pelo mais 4 caracteres!')

        if len(city) > 100:
            raise forms.ValidationError('O campo Cidade deve conter no máximo 100 caracteres!')
        
        return city
    
    def clean_state(self):
        state = self.cleaned_data.get('state')

        if len(state) < 4:
            raise forms.ValidationError('O campo Estado deve conter pelo mais 4 caracteres!')

        if len(state) > 80:
            raise forms.ValidationError('O campo Estado deve conter no máximo 100 caracteres!')
        
        return state