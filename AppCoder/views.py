from ast import Not
from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Series
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppCoder.forms import RegisterFormulario, reseniaFormulario
# Create your views here.

def inicio(request):

    return render(request, "index.html")

def register(request):

    form = RegisterFormulario(request.POST)
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
def addReseña(request):

    if request.method == 'POST':

        miFormulario=reseniaFormulario(request.POST, request.FILES)
        informacion = reseniaFormulario.cleaned_data
       
        if miFormulario.is_valid():

            estreno = Series(nombre=informacion['nombre'], reseña=informacion['reseña'], imagen=informacion['imagen'])

            estreno.save()

            return render(request, 'resenias/resenias.html')
    else:

        miFormulario=reseniaFormulario()


    return render(request,"resenias/aniadir.html", {'form':miFormulario})

@login_required
def reseñaBuscador(request):

    return render(request, "resenias/resenias.html")

@login_required
def buscar(request):
    if request.GET["reseña"]:

        nombre=request.GET['reseña']

        resultados=Series.objects.filter(nombre__icontains=nombre)

        return render(request, "resenias/resultadoBusqueda.html",{"resultados":resultados, "busqueda":nombre})

    else:
        respuesta="No enviaste datos."

    return HTTPResponse(respuesta)

@login_required
def reseniaDahmer(request):

    return render(request,"resenias/creadas/rdahmer.html")

@login_required
def reseniaSaul(request):

    return render(request,"resenias/creadas/saul.html")

@login_required
def reseniaBreaking(request):

    return render(request,"resenias/creadas/breaking.html")

@login_required
def reseniaDevil(request):

    return render(request,"resenias/creadas/devil.html")

@login_required
def reseniaWitcher(request):

    return render(request,"resenias/creadas/witcher.html")

@login_required
def reseniaBlacklist(request):

    return render(request,"resenias/creadas/blacklist.html")

@login_required
def reseniaOzark(request):

    return render(request,"resenias/creadas/ozark.html")

@login_required
def reseniaDark(request):

    return render(request,"resenias/creadas/dark.html")
