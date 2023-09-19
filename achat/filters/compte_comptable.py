import django_filters
from django_filters import CharFilter
from ..models import CompteComptable


class CompteFilter(django_filters.FilterSet):
    nom_compte = CharFilter(field_name='nom_compte',lookup_expr='icontains')
    class Meta:
        model = CompteComptable
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
       super(CompteFilter, self).__init__(*args, **kwargs)
       self.filters['nom_compte'].label="Nom du compte contient"