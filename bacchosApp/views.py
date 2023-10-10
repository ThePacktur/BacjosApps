from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    return HttpResponse("<h1>Welcome</h1>")

def displayDateTime(request):
    time = datetime.datetime.now()
    
    fecha = "<b>Fecha y Hora acutal: </b>" + str(time)
    return HttpResponse(fecha)

def renderTemplate1(request):
    data = {"nombre" : "PAcktur" }
    return render(request,'bacchosApp/holamundo.html',data)


def renderTemplate2(request):
    data = {"nombre" : "Algo" }
    return render(request,'bacchosApp/holamundo.html',data)

def infoUsuario(request):
    informacion = {"Id": "123","Nombre":"Clark Kent", "Email": "superman@jL.ong"}
    return render(request,'bacchosApp/userinfoTemplate.html',informacion)

def plantilla(request):
    return render(request, 'bacchosApp/plantilla.html')