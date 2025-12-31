import django_filters
from .models import Flower


class FlowerFilter(django_filters.FilterSet):
    color = django_filters.CharFilter(field_name='color',lookup_expr='iexact')
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    # id=django_filters.RangeFilter(field_name='flo_id')
    id_min = django_filters.CharFilter(method='filter_by_id_range',label='from flower ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label='To flower ID')
    
    class Meta:
        model = Flower
        fields = ['color' ,'name','id_min','id_max']
        
    def filter_by_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(flo_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(flo_id__lte=value)
        return queryset