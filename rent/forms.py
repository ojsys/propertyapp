from django import forms
from .models import Rent, PropertyInfo, Income, Expenses



class RentForm(forms.ModelForm):
    class Meta:
        GENDER = (
            ("F", "F"),
            ("M", "M"),
        )
        OWNER = (
            ("Owner 1", "Owner 1"),
            ("Owner 2", "Owner 2"),
            ("Owner 3", "Owner 3"),
            ("Owner 4", "Owner 4"),
        )
        model = Rent
        fields = ['name', 'phone', 'email', 'property_type', 'location', 'rent_rate', 'due_date', 'gender', 'owner']
        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email',
            'property_type': 'Property Type',
            'location': 'Location',
            'rent_rate': 'Rent Rate',
            'due_date': 'Due Date',
            'gender': 'Gender',
            'owner': 'Owner'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'rent_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }
    


class PropertyInfoForm(forms.ModelForm):
    class Meta:
        OWNER = (
            ("Owner 1", "Owner 1"),
            ("Owner 2", "Owner 2"),
            ("Owner 3", "Owner 3"),
            ("Owner 4", "Owner 4"),
        )
        model = PropertyInfo
        fields = ['property_name', 'property_type', 'property_location', 'property_description', 'property_owner', 'property_images']
        labels = {
            'property_name': 'Property Name',
            'property_type': 'Property Type',
            'property_location': 'Location',
            'property_description': 'Description',
            'property_owner': 'Owner',
            'property_images': 'Images',
        }
        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control'}),
            'property_location': forms.TextInput(attrs={'class': 'form-control'}),
            'property_description': forms.Textarea(attrs={'class': 'form-control'}),
            'property_owner': forms.Select(attrs={'class': 'form-control'}),
            'property_images': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple':True}),
        }



class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('payment_date', 'tenant', 'payment_desc', 'payment_amount')
        labels = {
            'payment_date': 'Payment Date',
            'tenant': 'Tenant Name', 
            'payment_desc': 'Payment Description', 
            'payment_amount': 'Amount', 
        
        }
        widgets = {
            'payment_date': forms.DateInput(attrs={'class': 'form-control'}),
            'tenant': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('payment_date', 'payment_method', 'paid_to', 'payment_desc', 'payment_amount')
        labels = {
            'payment_date': 'Payment Date',
            'payment_method': 'Payment Method',
            'paid_to': 'Payment To',
            'payment_desc': 'Payment Description', 
            'payment_amount': 'Amount', 
        
        }
        widgets = {
            'payment_date': forms.DateInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'paid_to': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
