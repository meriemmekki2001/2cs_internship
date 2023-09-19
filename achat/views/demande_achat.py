from datetime import date, datetime
import re
import time
import csv
import re
from django.urls import reverse
from django.core.files.base import ContentFile
from django.db.models import Case, Value, When
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import FileResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.core.files import File
import json
from django.urls import reverse
from django.conf import settings
import requests

from django.db.models import Q
from decimal import Decimal
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.core.mail import send_mail
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, DetailView
from django_filters.views import FilterView

from achat.filters import compte_comptable, comptecomptable_detail, demandeAchat
from achat.models.telechargement import Download

from ..filters import DemandeAchatFilter

from ..models import CompteComptable, CompteComptableDetails, DemandeAchat, Project, ProductPurchase, User, \
    GeneralHistorical, GeneralHistoricalDetail, DemandePaiment,Structure
from ..forms import DemandeAchatForm, ProductPurchaseForm,DemandePaimentForm



@login_required
def DemandeAchatForm_(request, id=0):
    if request.method == "GET":
        destination_achat = request.GET.get('destination_achat')
        nature_achat = request.GET.get('nature_achat')
        mise_dispo = request.GET.get('mise_dispo')
        affectation_achat = request.GET.get('affectation_achat')
        designations = request.GET.get('designations')
        qtts = request.GET.get('qtts')
        designations = eval(designations)
        qtts = eval(qtts)
        print(qtts[0])


        form = DemandeAchatForm()
        form.fields['destination_achat'].initial = destination_achat
        formPA = ProductPurchaseForm()
        projet__ = Project.objects.filter(Q(chef_projet=request.user.id) | Q(sponsor=request.user.id))

        compte_comptable = CompteComptable.objects.all()

        ctx = {}
        ctx['form'] = form
        ctx['formPA'] = formPA
        ctx['projet__'] = projet__
        ctx['comptes'] = compte_comptable
        ctx['logged_id'] = request.user.id
        ctx["mise_dispo"] = mise_dispo
        ctx["nature_achat"] = nature_achat
        ctx["affectation_achat"] = affectation_achat
        ctx["desi"] = designations
        ctx["qtt"] = qtts

        return render(request, "demandeAchat/demande_achat_create.html", ctx)
    else:

        form = DemandeAchatForm(request.POST)

        designations = request.POST['designations']
        code_comptable = json.loads(request.POST['code_comptable'])
        code_comptable_detail = json.loads(request.POST['code_comptable_detail'])

        grand_total = request.POST['grand_total']

        designation_list = json.loads(designations)
        fournisseurs = request.POST['fournisseurs']
        fournisseurs_list = json.loads(fournisseurs)
        prices = request.POST['prices']
        prices_list = json.loads(prices)
        Quantite = request.POST['qtys']
        Quantite_list = json.loads(Quantite)

        ID = 0
        try:
            if (DemandeAchat.objects.latest('id').DA_Code):
                ID = DemandeAchat.objects.latest('id')
                num = (ID.id) + 1
        except:
            ID = 0
            num = (ID) + 1
        import re
        num = 0
        
        for match in re.finditer(r"(?im)^\D*(\d+(?:[- ][a-z ]*[a-z])?)", DemandeAchat.objects.latest('id').DA_Code):
            yournumber = match.group(1)

            num = yournumber
        lastnum = 0
        firstnum=0
        for ch in num:
            firstnum=num[:2]
            lastnum = int(num[-5:])

        number = str(lastnum + 1).zfill(5)
        year = time.strftime("%y", time.localtime())
        if (firstnum < year):

            number = str(1).zfill(5)
        ##########
        demande__achat = DemandeAchat(DA_Code="{}".format("DA" + year + number),
                                      destination_achat=request.POST['destination_achat'],
                                      projet_id=request.POST['projet_id']
                                      , nature_achat=request.POST['nature_achat'],
                                      autre_nature_achat=request.POST['autre_nature_achat']
                                      , disponibilité=request.POST['disponibilité'],
                                      mise_dispo=request.POST['mise_dispo']
                                      , autre_mise_dispo=request.POST['autre_mise_dispo'],
                                      affectation_achat=request.POST['affectation_achat'],
                                      autre_affectation_achat=request.POST['autre_affectation_achat'],
                                      devise=request.POST['devise'],
                                      code_comptable_id=int(code_comptable),
                                      code_comptable_detail_id=int(code_comptable_detail),
                                      total_devis=float(grand_total.replace(',', '')), created_by_id=request.user.id,
                                      modified_by_id=request.user.id, statut_achat='001',
                                      etat_achat="En attente validation directeur")
        ######## SAVE LA DEMANDE ACHAT
        demande__achat.save()

        ID = DemandeAchat.objects.latest('id')
        demande = DemandeAchat.objects.filter(pk=ID.id).values()[0]

        emptyDict = {}
        # save_historique(request, ID.id, "DemandeAchat", "create", "all", emptyDict,
        #                 json.loads(json.dumps(demande, indent=4, sort_keys=True, default=str)))

        #### SAVE PRODUIT ACHAT
        for i in range(len(Quantite_list)):
            m = re.findall(r'\d+\.\d+', prices_list[i])

            if [] == m:
                produitachat = ProductPurchase(designation=designation_list[i], fournisseur=fournisseurs_list[i],
                                               price=prices_list[i], quantite=float(Quantite_list[i]), id_achat=ID)
                produitachat.save()

            else:


                my_float = float(m[0])
                # produitachat = ProductPurchase(designation=designation_list[i], fournisseur=fournisseurs_list[i],
                # price=float(prices_list[i]), quantite=int(Quantite_list[i]), id_achat=ID)
                produitachat = ProductPurchase(designation=designation_list[i], fournisseur=fournisseurs_list[i],
                                               price=my_float, quantite=float(Quantite_list[i]), id_achat=ID)
                produitachat.save()



            ########
        demande_destination_achat = DemandeAchat.objects.get(pk=ID.id)

        #### SENDING MAILS
        # send_mail_first_directeur_resp(request, ID, demande_destination_achat.destination_achat)
        return HttpResponseRedirect('/achat/demandeachat/myachat')


def ajax_load_detail(request):
    
    id_devise = request.GET.get('id_devise')
    id_destination_achat = request.GET.get('id_destination_achat')
    structure_user = request.user.departement

    details = CompteComptableDetails.objects.filter(devise=id_devise,
                                                    destination_achat_compte=id_destination_achat,
                                                    structure=structure_user,status='Actif').all()

    return render(request, 'demandeAchat/detail_drop-down.html', {'details': details})

def ajax_load_compte_comptable(request):
    
    id_code_comptable_detail = request.GET.get('id_code_comptable_detail')
    

    

    compte_en_detail = CompteComptableDetails.objects.get(pk=id_code_comptable_detail)
  
    
    


    return render(request, 'demandeAchat/compte_comptable_drop-down.html', {'compte': compte_en_detail.code_comptable})


def ajax_load_detail_projet(request):
    #id_code_comptable = request.GET.get('id_code_comptable')
    id_devise = request.GET.get('id_devise')
    id_destination_achat = request.GET.get('id_destination_achat')
    id_projet=request.GET.get('projet')
    structure_user = request.user.departement

    #details = CompteComptableDetails.objects.filter(code_comptable=id_code_comptable, devise=id_devise,
                                                   # destination_achat_compte=id_destination_achat,
                                                   # structure=structure_user).all()
    projets = Project.objects.filter(pk=id_projet).values('compte_comptable_detail')

    deta=CompteComptableDetails.objects.filter(pk__in=projets, devise=id_devise,
                                                    destination_achat_compte=id_destination_achat,
                                                    structure=structure_user,status='Actif').all()

    return render(request, 'demandeAchat/detail_drop-down.html', {'details': deta})


