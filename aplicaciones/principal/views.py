from django.shortcuts import render
from .models import Persona

# Create your views here.
def inicio(request):
    personas = Persona.objects.all()  #select * from Persona
    contexto = {
        'personas':personas
    }
    return render(request, 'index.html',contexto)

def crearPersona(request):
    return render(request, 'create_persona.html')

