from django.views.generic import CreateView, ListView
from deliveries.models import DeliveryRequest
from deliveries.forms import DeliveryRequestModelForm

class ListDeliveryRequestsView(ListView):
    ...

class CreateDeliveryRequestView(CreateView):
    model = DeliveryRequest
    form_class = DeliveryRequestModelForm
    template_name = 'delivery_request.html'
    success_url = 'delivery_requests'
