from django.shortcuts import render, redirect
from .models import PreDemande
from .forms import PreDemandeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from comptes.models import User

def index(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    predemandes = PreDemande.objects.all()
    if request.user.is_authenticated:
       return render(request, 'core/index.html', {'predemandes': predemandes})
    else:
       return render(request, 'comptes/dashboard.html')
       


def create_predemande(request):
    if request.method == 'POST':
        form = PreDemandeForm(request.POST)
        if form.is_valid():
            pre_demande = form.save(commit=False)
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            pre_demande.cree_par = user
            pre_demande.departement = user.departement   
            pre_demande.save()
            return redirect('core:index')  
    else:
        form = PreDemandeForm()
    return render(request, 'core/create.html', {'form': form,'success':True})


def edit(request, id):
  if request.method == 'POST':
    pre_demande = PreDemande.objects.get(pk=id)
    form = PreDemandeForm(request.POST, instance=pre_demande)
    if form.is_valid():
      form.save()
      return render(request, 'core/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = PreDemande.objects.get(pk=id)
    form = PreDemandeForm(instance=student)
  return render(request, 'core/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    pre_demande = PreDemande.objects.get(pk=id)
    pre_demande.delete()
  return HttpResponseRedirect(reverse('core:index'))
