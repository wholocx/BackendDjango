from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'indexx.html')

def logging_in(request):
    return render(request, 'vhod\\registration.html')

def lk(request):
    return render(request, 'LK_OSNOVA.html')

def registration(request):
    return render(request, 'registracia\\login.html')

def predlojenie1(request):
    return render(request, 'Sidenav\\arenda_traktori.html')

def kombainiArenda(request):
    return render(request, 'Sidenav\\arenda_kombaini.html')

def opriskivateliArenda(request):
    return render(request, 'Sidenav\\arenda.opriskivateli.html')

def kombProd(request):
    return render(request, 'Sidenav\\prodazha_kombaini.html')

def oprisProd(request):
    return render(request, 'Sidenav\\prodazha_opriskivateli.html')

def trakProd(request):
    return render(request, 'Sidenav\\prodazha_traktori.html')

def changeLK(request):
    return render(request, "LK_IZM.html")