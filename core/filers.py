import django_filters
from .models import Book
from django import forms


class BookFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
      
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(BookFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['genre'].field.widget.attrs.update({
        'class':"custom-select mr-sm-2"
        })
        self.filters['tradeType'].field.widget.attrs.update({
        'class':"custom-select mr-2"
        }) 
        self.filters['name'].field.widget.attrs.update({
        'class':"form-control mr-sm-2",
        'type':"text",
        'name':"TorA",
        'placeholder':"Cherchez par titre",
        'id':"formGroupExampleInputMD"
        })  

    class Meta:
        model = Book
        fields = ('name', 'genre', 'tradeType')