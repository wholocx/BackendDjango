from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Agrotech.forms import CreateUserForm


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
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            validation = False
            if(len(password1) <=7):
                messages.error(request, 'Пароль должен быть не менее 8 символов!')
            elif(password1 != password2):
                messages.error(request, 'Пароли не совпадают!')
            elif(('@' in email) == False):
                messages.error(request, 'Пароли не совпадают!')
            else:
                validation = True
            if validation == True:
                user= User.objects.create_user(username, email, password1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                messages.success(request, username + ', вы успешно зарегистрированы!')
                print('Все ок')
                return redirect('login')
            


        return render(request, 'registracia\\login.html', ctx)

@login_required(login_url = 'login')
def changeLK(request):   
    if(request.method == 'POST'):
        form = PasswordChangeForm(data = request.POST, user=request.user)
        if (form.is_valid()):
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, "Пароль успешно изменен!")
            return redirect('changeData')
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form': form}
        return render(request, 'LK_IZM.html', args)





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

