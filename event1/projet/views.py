from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Evenement
from django.utils.dateparse import parse_datetime
from django.contrib import messages

#@login_required
#@require_http_methods(["GET", "POST"])
def creer_evenement(request):
    if request.method == 'POST':
        if request.user.utilisateur.ROLE != 'organisateur':
            messages.error(request, "Vous n'avez pas les droits pour créer un événement.")
            return redirect('')  # Redirect to an appropriate page
        try:
            event = Evenement(
                id_organisateur = request.ID_UTILISATEUR,
                titre=request.POST['titre'],
                description=request.POST.get('description'),
                lieu=request.POST.get('lieu'),
                date_evenement=parse_datetime(request.POST['date_evement']),
                capacite=int(request.POST['capacite']),
                programme=request.POST.get('programme'),
                image=request.POST.get('image')
            )
            event.save()
            return JsonResponse({'status': 'success', 'message': 'Evenement créer avec succès'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return render(request, 'projet/creer_evenement.html')

# def liste_evenements(request):
#     evenements = Evenement.objects.all()
#     return render(request, 'liste_evenements.html', {'evenements': evenements})

# def update_evenement(request, evenement_id):
#     evenement = get_object_or_404(Evenement, id=evenement_id)
#     erreur = None
    
#     user = request.user
        
#         # Si l'utilisateur connecté n'a pas d'organisateur associé, l'attribuer
#     organisateur, created = Organisateur.objects.get_or_create(user=user)
#     if request.method == 'POST':
#         titre = request.POST.get('titre')
#         description = request.POST.get('description')
#         date_evenement = parse_date(request.POST.get('date_evenement'))
#         lieu = request.POST.get('lieu')
#         capacite = request.POST.get('capacite')
#         programme = request.POST.get('programe')
#         organisateur = request.POST.get('organisateur')
#         image = request.FILES.get('image')

#         if not titre or not date_evenement or not lieu or not organisateur:
#             erreur = "Tous les champs obligatoires (*) doivent être remplis."
#         else:
            
#             evenement.titre = titre
#             evenement.description = description
#             evenement.date_evenement = date_evenement
#             evenement.lieu = lieu
#             evenement.capacite = capacite
#             evenement.programme = programme
#             evenement.organisateur = organisateur
#             if image:
#                 evenement.image = image
#             evenement.save()
#             return redirect('liste_evenements')

#     return render(request, 'update_evenement.html', {'evenement': evenement,'erreur': erreur})

# def delete_evenement(request, evenement_id):
#     evenement = get_object_or_404(Evenement, id=evenement_id)

#     # Vérifier si l'utilisateur connecté est l'organisateur de l'événement
#     if evenement.organisateur.user != request.user:
#         return redirect('liste_evenements')  # Rediriger si ce n'est pas l'organisateur

#     if request.method == 'POST':
#         evenement.delete()
#         return redirect('liste_evenements')

#     return render(request, 'delete_evenement.html', {'evenement': evenement})

def index(request):
    return render(request, 'projet/index.html')

def inscription(request):
    if request.method =='POST':
        nom= request.POST.get('nom')
        email = request.POST.get('email')
        mdp = request.POST.get('mdp')
        role = request.POST.get('role')

        user = Utilisateur(
            nom_utilisateur=nom,
            email_utilisateur= email,
            mdp_utilisateur=mdp,
            role=role   
        )
        user.save()
        return redirect('/')
    return render(request, 'projet/inscription.html')

def connexion(request):
    return render(request, 'projet/connexion.html')

def event_list(request):
    event = Evenement.objects.all().order_by('date_evenement')
    return render(request, 'projet/event_list.html', {'evenements': event})
