
from django.contrib import admin
from django.urls import path
from cars.views import CreateCarView, ListCarsView, ListBrandView, CreateBrandView, ListVehicleTypeView, CreateVehicleTypeView, UptadeCarView, DeleteCarView, UpdateBrandView, DeleteBrandView, UpdateVehicleTypeView, DeleteVehicleTypeView
from customers.views import CreateCustomerView, ListCustomersView, UpdateCustomerView, DeleteCustomerView, DetailCustomerView, CreateAddressView, DeleteAddressView
from deliveries.views import CreateDeliveryRequestView
from accounts.views import LoginView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login' ),
    path('signup/', SignupView.as_view(), name='signup' ),
    path('cars/', ListCarsView.as_view(), name='cars_list' ),
    path('car_create/', CreateCarView.as_view(), name='car_create'),
    path('car/<int:pk>/update', UptadeCarView.as_view(), name='car_update' ),
    path('car/<int:pk>/delete', DeleteCarView.as_view(), name='car_delete' ),
    path('brands/', ListBrandView.as_view(), name='brands_list'),
    path('brand_create/', CreateBrandView.as_view(), name='brand_create'),
    path('brand/<int:pk>/update', UpdateBrandView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete', DeleteBrandView.as_view(), name='brand_delete'),
    path('vehicle_types/', ListVehicleTypeView.as_view(), name='vehicle_types_list'),
    path('vehicle_type_create/', CreateVehicleTypeView.as_view(), name='vehicle_type_create'),
    path('vehicle_type/<int:pk>/update', UpdateVehicleTypeView.as_view(), name='vehicle_type_update'),
    path('vehicle_type/<int:pk>/delete', DeleteVehicleTypeView.as_view(), name='vehicle_type_delete'),
    path('customers', ListCustomersView.as_view(), name='customers_list'),
    path('customer_create', CreateCustomerView.as_view(), name='customer_create'),
    path('customer/<int:pk>/update', UpdateCustomerView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete', DeleteCustomerView.as_view(), name='customer_delete'),
    path('customer/<int:pk>/detail', DetailCustomerView.as_view(), name='customer_detail'),
    path('custumer/<int:customer_id>/address_create', CreateAddressView.as_view(), name="address_create"),
    path('address/<int:pk>/address_delete', DeleteAddressView.as_view(), name="address_delete"),
    path('delivery_request', CreateDeliveryRequestView.as_view(), name='delivery_request'),
]
