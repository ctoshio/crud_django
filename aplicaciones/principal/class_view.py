from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona

"""
Example
class ListView(View):
    model = Persona
    Template_name = 'index.html'

    #Django automatically execute the code below 

    ListView: # this defs are black box ListView
    def dispatch()

    def get_context_data(self):
        context = {}
        context['queryset'] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all() #specify model

    def get_templates_names():
        return self.template_name #specify template_name

    def get(self, request,*args,**kwargs):
        return render(request, self.get_templates_names(), self.get_context_data())


#############
    def post(self, request,*args,**kwargs):

    dispatch : verificar el metodo de la solicitud http
    http_not_allowed
"""
class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm 
    template_name = 'create_persona.html'
    success_url = reverse_lazy('index')   

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm 
    template_name = 'create_persona.html'
    success_url = reverse_lazy('index')    