from django import forms
from django.db.models.fields.related import ForeignObject
from django.forms import ModelForm
from django.db.models import fields
from .models import *

class edit_form(forms.ModelForm):
    class Meta:
        model=Req_info
        fields = ['status', 'Name_Costomer','Postal_Address','GrandTotal']

class edit_form1(forms.ModelForm):
    class Meta:
        model=Product
        fields = ['name','price', 'Quantity']
        

class delete_form(forms.ModelForm):
    class Meta:
        model= Feedback
        fields = "__all__"

class Profile(forms.ModelForm):
    class Meta:
        model= User
        fields = [ 'username', 
            'first_name', 
            'last_name', 
            'email',
            ]

class Profileextend(forms.ModelForm):
    class Meta:
        model= Customers
        fields = [ 'phone', 
            'Address',
            'profile_pic',
            
            ]