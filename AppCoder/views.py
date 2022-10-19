from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppCoder.forms import RegisterFormulario
# Create your views here.

def inicio(request):

    return render(request, "index.html")

def register(request):

    form = RegisterFormulario(request.POST or None)
    if request.method == 'POST':
        

        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()

            return render(request,"homepage.html")

        else:
            form = RegisterFormulario()

    return render(request,"autenticar/register.html", {'form':form})


def iniciarSesion(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render(request,"homepage.html")

        else: 

            return render(request,"homepage.html", {'mensaje':"Datos incorrectos"})

    else:

        form = AuthenticationForm()
 
    return render(request,"autenticar/iniciarSesion.html", {'form':form})

@login_required
def home(request):

    return render(request,"homepage.html")

@login_required
def about(request):

    return render(request,"about.html")

@login_required
def reseña(request):

    return render(request,"resenias.html")

