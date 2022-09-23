from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario
# Create your views here.

def inicio(request):

    return render(request,"index.html")

def cursos(request):

    cursoPython = Curso(nombre="Python", camada=41635)
    cursoPython.save()

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info["camada"])

            curso.save()

            return render(request, "index.html")
    
    else:
        formulario1 = CursoFormulario()

    return render(request,"cursos.html", {"form1":formulario1})


def estudiantes(request):

    return render(request,"estudiantes.html")

def resultados(request):
    
    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact=camada)

        return render(request, "estudiantes.html", {"cursos":cursos, "camada":camada})
    
    else:

        respuesta = "No hay datos ingresados."

    return HTTPResponse(respuesta)

def entregables(request):

    return render(request,"entregables.html")

