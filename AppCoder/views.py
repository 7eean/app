from re import template
from django.template import loader
from AppCoder.models import MyFamily
from django.http import HttpResponse
# Create your views here.

def family(request):

    mama = MyFamily(nombre = "Matilde", edad = 49, fechaCumple = '2022-12-15',)
    mama.save() 

    abuela = MyFamily(nombre = "Julia", edad = 79, fechaCumple = '2022-7-13',)
    abuela.save()

    papa = MyFamily(nombre= "Ivan", edad = 47, fechaCumple = '2022-8-9',)
    papa.save()

    contexto = {"mama":mama, "abuela":abuela, "papa":papa }


    # miHtML = open("C:/Users/gomez/Desktop/Coding/Python/ProyectoCoder/AppCoder/templates/index.html")
    # plantilla = Template(miHtML.read())
    # miHtML.close()
    # miContexto = Context(family)
    # documento = plantilla.render(miContexto)
    # return HttpResponse(documento)

    plantilla = loader.get_template("index.html")
    
    documento = plantilla.render(contexto)

    return HttpResponse(documento)



    # return HttpResponse(f"Mi mama se llama {mama.nombre}, tiene la edad de: {mama.edad} y su cumple es el dia {mama.fechaCumple}")




