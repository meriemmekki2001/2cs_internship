import django_filters
from django_filters import CharFilter
from ..models import DemandeAchat


class DemandeAchatFilter(django_filters.FilterSet):
    DA_Code = CharFilter(field_name='DA_Code',lookup_expr='icontains')
    class Meta:
        model = DemandeAchat
        fields = ('destination_achat', 'devise', 'statut_achat', 'created_by__departement','DA_Code')

    def __init__(self, *args, **kwargs):
        super(DemandeAchatFilter, self).__init__(*args, **kwargs)
        self.filters['created_by__departement'].label = "Structure"


