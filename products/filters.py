from . models import Product, Category
import django_filters
from django_filters.filters import RangeFilter
from django import forms


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='',max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'поиск продукта'}))
    #price = RangeFilter()


    class Meta:
        model = Product
        fields = ['name']

class CategoryFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains', label='',max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'введите раздел поиска, например: коробка'}))
 
    class Meta:
        model = Category
        fields = ['name']







