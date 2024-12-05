from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Evenement, Organisateur
from django.utils.dateparse import parse_date

def creer_evenement(request):
    erreur = None
    user = request.user
        
        # Si l'utilisateur connecté n'a pas d'organisateur associé, l'attribuer
    organisateur, created = Organisateur.objects.get_or_create(user=user)
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date_evenement = parse_date(request.POST.get('date_evenement'))
        lieu = request.POST.get('lieu')
        capacite = request.POST.get('capacite')
        programme = request.POST.get('programe')
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
                id_organisateur=organisateur,
                image = image,
            )
            evenement.save()
            return redirect('liste_evenements')  # Redirige vers une liste d'événements (ou une autre page)

    return render(request, 'creer_evenement.html', {'erreur': erreur})

def liste_evenements(request):
    evenements = Evenement.objects.all()
    return render(request, 'liste_evenements.html', {'evenements': evenements})

def update_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    erreur = None
    organisateurs = Organisateur.objects.all()

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
            organisateur = Organisateur.objects.get(id=organisateur)
            evenement.titre = titre
            evenement.description = description
            evenement.date_evenement = date_evenement
            evenement.lieu = lieu
            evenement.capacite = capacite
            evenement.programme = programme
            evenement.organisateur = organisateur
            if image:
                evenement.image = image
            evenement.save()
            return redirect('liste_evenements')

    return render(request, 'update_evenement.html', {'evenement': evenement, 'organisateurs': organisateurs, 'erreur': erreur})
