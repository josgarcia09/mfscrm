from django.contrib import admin
from .models import Customer, Service, Product

#Define the admin options for the Customer table
class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'phone' )
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

#Define the admin options for the Service table
class ServiceList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'service_category', 'setup_time')
    list_filter = ( 'cust_name', 'setup_time')
    search_fields = ('service_category','cust_name', )
    ordering = ['cust_name']

#Define the admin options for the Product table
class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'description', 'quantity', 'pickup_time', 'product_charge')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('description', 'cust_name', )
    ordering = ['cust_name']

admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)
