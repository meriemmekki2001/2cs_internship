from django.shortcuts import render, redirect,get_object_or_404
from .models import PreDemande,Categorie,Fournisseur,Produit
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotAllowed
from django.urls import reverse
from comptes.models import User,Structure
from .forms import ProduitFormSet,PreDemandeForm,CategorieForm, FournisseurForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core import serializers
import json
from django.core import serializers
from urllib.parse import urlencode

#display les pre demandes d'achats
def index(request):
    if request.user.is_authenticated:
       user = User.objects.get(pk=request.user.id)
       if user.departement.nom == 'Moyens Généraux':
           predemandes = PreDemande.objects.filter(Q(statut=PreDemande.Statut.VALIDEE_DS) | Q(statut=PreDemande.Statut.CLOTUREE), destinationCompte='MGX').order_by('-creee_le')
       elif user.departement.nom == 'Interconnexions':
            predemandes = PreDemande.objects.filter(Q(statut=PreDemande.Statut.VALIDEE_DS) | Q(statut=PreDemande.Statut.CLOTUREE),destinationCompte='INT').order_by('-creee_le')
       elif user.responsable:
            predemandes = PreDemande.objects.filter(departement=user.departement).order_by('-creee_le')
       else:
            predemandes = PreDemande.objects.filter(cree_par=user).order_by('-creee_le')

       return render(request, 'core/home.html', {'predemandes': predemandes, 'user': user})
    else:
       return render(request, 'comptes/access_denied.html')
       

# ajouter pre demande d'achat
def create_pre_demande(request):
    if request.method == 'POST':
        pre_demande_form = PreDemandeForm(request.POST)
        produit_formset = ProduitFormSet(request.POST, instance=PreDemande())

        if pre_demande_form.is_valid() and produit_formset.is_valid():
            pre_demande = pre_demande_form.save()
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            produit_formset.instance = pre_demande
            pre_demande.cree_par = user
            pre_demande.departement = user.departement
            pre_demande.save()
            produit_formset.save()
            return redirect('core:index')

    else:
        pre_demande_form = PreDemandeForm()
        produit_formset = ProduitFormSet(instance=PreDemande())

    context = {
        'pre_demande_form': pre_demande_form,
        'produit_formset': produit_formset,
    }

    return render(request, 'core/create_pda.html', context)

#validation d'une pre demande d'achat par un directeur de structure
def validation_ds(request, id):
    if request.method == 'POST':
      pre_demande = PreDemande.objects.get(pk=id)
      pre_demande.statut = PreDemande.Statut.VALIDEE_DS
      pre_demande.save()
      return HttpResponseRedirect(reverse('core:index'))
    
# rejet d'une pda par un directeur de structure   
def rejet_ds(request, id):
    if request.method == 'POST':
      pre_demande = PreDemande.objects.get(pk=id)
      pre_demande.statut = PreDemande.Statut.CLOTUREE
      pre_demande.reponse_finale = PreDemande.Reponse.REJETEE_DS
      pre_demande.save()
      return HttpResponseRedirect(reverse('core:index'))
    
#validation d'une pre demande d'acaht par un serivce d'achat
def validation_sa(request, id):
    if request.method == 'POST':
      pre_demande = PreDemande.objects.get(pk=id)
      pre_demande.statut = PreDemande.Statut.CLOTUREE
      pre_demande.reponse_finale = PreDemande.Reponse.VALIDEE_SA
      pre_demande.save()
      ctx = {}
      ctx['destination_achat'] = pre_demande.destinationCompte
      ctx['nature_achat'] = pre_demande.natureAchat
      ctx['mise_dispo'] = pre_demande.miseDiso
      ctx['affectation_achat'] = pre_demande.affectationAchat
      produits = Produit.objects.filter(pre_demande=pre_demande)
      designations = []
      qtts = []
      for produit in produits:
         designations.append(produit.designation)
         qtts.append(str(produit.qtt))
      ctx['designations'] = designations
      ctx['qtts'] = qtts
      url = reverse('demandeachat_create') + '?' + '&'.join([f'{key}={value}' for key, value in ctx.items()])

      return redirect(url)

# rejet d'une pre demande d'acaht par un serivce d'achat   
def rejet_sa(request, id):
    if request.method == 'POST':
      pre_demande = PreDemande.objects.get(pk=id)
      pre_demande.statut = PreDemande.Statut.CLOTUREE
      pre_demande.reponse_finale = PreDemande.Reponse.REJETEE_DS
      pre_demande.save()
      return HttpResponseRedirect(reverse('core:index'))
    

def create_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:list_fournisseurs')  
    else:
        form = FournisseurForm()
    return render(request, 'core/create_fournisseur.html', {'form': form})



def list_fournisseur(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'core/list_fournisseur.html', {'fournisseurs': fournisseurs})


def delete_fournisseur(request, id):
  if request.method == 'POST':
    fournisseur = Fournisseur.objects.get(pk=id)
    fournisseur.delete()
  return HttpResponseRedirect(reverse('core:list_fournisseurs'))



def list_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'core/list_categories.html', {'categories': categories})

def create_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:list_categories')  
    else:
       form = CategorieForm()
    
    return render(request, 'core/create_categorie.html', {'form': form})
    

def delete_categorie(request, id):
  if request.method == 'POST':
    categorie = Categorie.objects.get(pk=id)
    categorie.delete()
  return HttpResponseRedirect(reverse('core:list_categories'))



def annuler_pda(request, id):
    if request.method == 'POST':
      pre_demande = PreDemande.objects.get(pk=id)
      if request.user.id == pre_demande.cree_par.id:
         pre_demande.statut = PreDemande.Statut.ANNULEE
         pre_demande.save()
         return HttpResponseRedirect(reverse('core:index'))
      else:
         return HttpResponseNotAllowed(['GET'])


