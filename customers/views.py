from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from customers.models import Customer
from customers.forms import CustomerModelForm

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

class UpdateCustomerView(UpdateView):
    ...

class DeleteCustomerView(DeleteView):
    ...