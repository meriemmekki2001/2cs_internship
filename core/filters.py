import django_filters
from .models import PreDemande


class PreDemandeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = PreDemande
        fields = ["designation", "qtt"]
        