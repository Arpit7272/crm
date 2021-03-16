from django.db.models.fields import DateField
from .models import Order
import django_filters

class OrderFilter(django_filters.FilterSet):
    DateField = django_filters.DateFilter(field_name= "date_created", lookup_expr= 'gte')
    
    class Meta:
        model= Order
        exclude= ['customer','date_created',]


class OrderFilterAll(django_filters.FilterSet):
    DateField = django_filters.DateFilter(field_name= "date_created", lookup_expr= 'gte')
    
    class Meta:
        model= Order
        exclude= ['date_created']