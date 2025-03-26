from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from customers.models import Customer, Address
from customers.forms import CustomerModelForm, AddressForm

class ListCustomersView(ListView):
    model = Customer
    template_name = 'customers.html'
    context_object_name = 'customers'

    def get_queryset(self):
        customers = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')

        if search:
            customers = customers.filter(model__icontains=search)
        
        return customers

class CreateCustomerView(CreateView):
    model = Customer
    form_class = CustomerModelForm
    template_name = 'customer_create.html'
    success_url = 'customers'

class CreateAddressView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'address_create.html'

    def form_valid(self, form):
        customer = get_object_or_404(Customer, pk=self.kwargs["customer_id"])
        form.instance.customer = customer
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.kwargs['customer_id']})


class DeleteAddressView(DeleteView):
    model = Address
    template_name = 'address_delete.html'

    def get_success_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.object.customer_id})  

    

class UpdateCustomerView(UpdateView):
    model = Customer
    form_class = CustomerModelForm
    template_name = 'customer_update.html'
    success_url = 'detail'
    
class DeleteCustomerView(DeleteView):
    ...

class DetailCustomerView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    # context_object_name = 'customer'