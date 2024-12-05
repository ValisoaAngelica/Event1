from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import render, redirect
from .models import Evenement
from django.utils.dateparse import parse_date, parse_time

def creer_evenement(request):
    erreur = None

    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date_evenement = parse_date(request.POST.get('date_evenement'))
        lieu = request.POST.get('lieu')
        capacite = request.POST.get('capacite')
        programme = request.POST.get('programe')
        organisateur = request.POST.get('organisateur')
        image = request.FILES.get('image')
        if not titre or not date_evenement or not lieu or not organisateur:
            erreur = "Tous les champs obligatoires (*) doivent être remplis."
        else:
            evenement = Evenement(
                titre=titre,
                description=description,
                lieu=lieu,
                date_evenement=date_evenement,
                capacite = capacite,
                programme = programme,
                organisateur=organisateur,
                image = image,
            )
            evenement.save()
            return redirect('liste_evenements')  # Redirige vers une liste d'événements (ou une autre page)

    return render(request, 'creer_evenement.html', {'erreur': erreur})

