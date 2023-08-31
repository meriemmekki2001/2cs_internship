from django.shortcuts import render, redirect
from .models import PreDemande
from .forms import PreDemandeForm

def create_predemande(request):
    if request.method == 'POST':
        form = PreDemandeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('core:pre_demande_list')  
    else:
        form = PreDemandeForm()
    return render(request, 'core/create.html', {'form': form})

def pre_demande_list(request):
    predemandes = PreDemande.objects.all()
    return render(request, 'core/list.html', {'predemandes': predemandes})
