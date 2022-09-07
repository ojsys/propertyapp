from django.contrib import admin
from .models import Rent, PropertyInfo, Income, Expenses

class RentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'location', 'created_at', ]
    search_fields = ['name', 'phone', 'email', 'location']
    list_per_page: 10


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'property_type', 'property_location', 'property_description', 'property_owner' ]
    search_fields = ['property_name', 'property_type', 'property_location',]
    list_per_page: 10


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['payment_date', 'tenant', 'payment_desc', 'payment_amount', ]
    search_fields = ['payment_date', 'tenant', 'payment_desc', 'payment_amount', ]
    list_per_page: 10


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['payment_date', 'payment_method', 'paid_to', 'payment_desc', 'payment_amount', ]
    search_fields = ['payment_date', 'payment_method', 'paid_to', 'payment_desc', 'payment_amount',]
    list_per_page: 10


admin.site.register(Rent, RentAdmin)
admin.site.register(PropertyInfo, PropertyAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expenses, ExpensesAdmin)