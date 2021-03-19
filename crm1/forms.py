from django.forms import ModelForm
from .models import Order, Customer, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:

        model = Order
        fields = '__all__'


class CustomerForm(ModelForm):

    class Meta:
               
        model = Customer
        fields = '__all__'
        exclude = ['user']


class ProductForm(ModelForm):

    class Meta:
        model= Product
        fields = '__all__'
        exclude=['date_created']

