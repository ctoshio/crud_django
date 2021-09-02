from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def inicio(request):
    personas = Persona.objects.all()  #select * from Persona
    contexto = {
        'personas':personas
    }
    return render(request, 'index.html',contexto)

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        print(form)
    return render(request, 'create_persona.html', contexto)

