from email.policy import default
from django.db import models


class Owner(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'



class Rent(models.Model):
    """Creates a new rent object with fullname, phone number, email address, gender, location, and property owner information"""
    GENDER = (
        ("F", "F"),
        ("M", "M"),
    )
    
    
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rent_rate = models.CharField(max_length=255)
    due_date = models.DateField()
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    owner = models.ForeignKey(Owner, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to='media/', default=None, null=True, blank=True)


    def __str__(self):
        return f'{self.name}'




class PropertyInfo(models.Model):
    
    property_name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    property_location = models.CharField(max_length=255)
    property_description = models.CharField(max_length=255)
    property_owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)
    property_images = models.ImageField(upload_to='images/')


    def __str__(self):
        return f'{self.property_name}'



class Income(models.Model):
    payment_date = models.DateField()
    tenant = models.CharField(max_length=255, blank=True)
    payment_desc = models.CharField(max_length=255, blank=True)
    payment_amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.tenant} - {self.payment_amount} - {self.payment_desc}'


class Expenses(models.Model):
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=255, blank=True)
    paid_to = models.CharField(max_length=255, blank=True)
    payment_desc = models.CharField(max_length=255, blank=True)
    payment_amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.paid_to} - {self.payment_amount} - {self.payment_date}'


