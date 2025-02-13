from django.shortcuts import render
from .models import PieceDisparue
# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')

def liste_pieces(request):
    pieces = PieceDisparue.objects.all()
    return render(request, 'liste_pieces.html', {'pieces': pieces})

def declare_perte(request):
    return render(request,'form.html')

def recherche(request):
    return render(request,'search.html')