import django_filters

from ..models import CompteComptableDetails


class CompteDetailFilter(django_filters.FilterSet):
    class Meta:
        model = CompteComptableDetails
        fields = ('destination_achat_compte','devise','structure')

        labels = {

            
            
            'destination_achat_compte':'Destination ',
            'devise':'Devise',
            'structure':'Structure'



        }