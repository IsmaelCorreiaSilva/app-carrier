from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from cars.models import Car, Brand, VehicleType
from cars.forms import CarModelForm, BrandModelForm, VehicleTypeModelForm

class ListCarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars =  super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains = search)

        return cars

class CreateCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_create.html'
    success_url = '/cars/'

class UptadeCarView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

    # def get_success_url(self):
    #     return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

class ListBrandView(ListView):
    model = Brand
    template_name = 'brands.html'
    context_object_name = 'brands'

class CreateBrandView(CreateView):
    model = Brand
    form_class = BrandModelForm
    template_name = 'brand_create.html'
    success_url = '/brands/'

class UpdateBrandView(UpdateView):
    model = Brand
    form_class = BrandModelForm
    template_name = 'brand_update.html'
    success_url = '/brands/'


class DeleteBrandView(DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = '/brands/'

class ListVehicleTypeView(ListView):
    model = VehicleType
    template_name = 'vehicle_types.html'
    context_object_name = 'vehicle_types'

class CreateVehicleTypeView(CreateView):
    model = VehicleType
    form_class = VehicleTypeModelForm
    template_name = 'vehicle_type_create.html'
    success_url = '/vehicle_types/'

class UpdateVehicleTypeView(UpdateView):
    model = VehicleType
    form_class = VehicleTypeModelForm
    template_name = 'vehicle_type_update.html'
    success_url = '/vehicle_types/'

class DeleteVehicleTypeView(DeleteView):
    model = VehicleType
    template_name = 'vehicle_type_delete.html'
    success_url = '/vehicle_types/'
    
