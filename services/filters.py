from .models import Services
import django_filters

class ServicesFilter(django_filters.FilterSet):
    class Meta:
        model = Services
        fields = '__all__'
        exclude = ['image']