from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm


def index(request):
    return render(request, 'indexx.html')

def logging_in(request):
    if request.user.is_authenticated:
        return redirect('user')
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)        
            if user is not None:
                login(request, user)
                return redirect('user')
            else:
                messages.info(request, 'Имя пользователя или пароль неверны')
        context = {}
        return render(request, 'vhod\\registration.html', context)

@login_required(login_url = 'login')
def lk(request):
    
    return render(request, 'LK_OSNOVA.html')

def registration(request):

    if request.user.is_authenticated:
        return redirect('user')
    else:
        form = CreateUserForm()   
        
        ctx = {'form': form}
        if (request.method == 'POST'):
            form = CreateUserForm(request.POST)
            password = form['password1']

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ', вы успешно зарегистрированы!')
                return redirect('login')
            elif(len(password) <=7):
                messages.error(request, 'Пароль должен быть не менее 8 символов!')
            


        return render(request, 'registracia\\login.html', ctx)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def predlojenie1(request):
    return render(request, 'Sidenav\\arenda_traktori.html')

@login_required(login_url = 'login')
def kombainiArenda(request):
    return render(request, 'Sidenav\\arenda_kombaini.html')

@login_required(login_url = 'login')
def opriskivateliArenda(request):
    return render(request, 'Sidenav\\arenda.opriskivateli.html')

@login_required(login_url = 'login')
def kombProd(request):
    return render(request, 'Sidenav\\prodazha_kombaini.html')

@login_required(login_url = 'login')
def oprisProd(request):
    return render(request, 'Sidenav\\prodazha_opriskivateli.html')

@login_required(login_url = 'login')
def trakProd(request):
    return render(request, 'Sidenav\\prodazha_traktori.html')

@login_required(login_url = 'login')
def changeLK(request):
    return render(request, "LK_IZM.html")