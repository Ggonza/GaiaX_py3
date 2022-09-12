from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.http import request
from django.shortcuts import render

from core.comedor.forms import ListasUsuForm
from core.comedor.models import Profesor, Estudiante, Curso, ListaUsc


class listEstudentsView(ListView):
    model = Estudiante
    template_name = 'profesor/profesorP.html'

    def get_queryset(self):
        return Estudiante.objects.all()

    def get_context_data(self, **kwargs):
        cursoVar = Curso.no_curso
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'G-Profesor'
        context['curso'] = cursoVar
        return context

class ListaCreateView(CreateView):
    model = ListaUsc, Estudiante
    form_class = ListasUsuForm
    template_name = 'profesor/profesorP.html'
    success_url = reverse_lazy('comedor:listasUsc')

    def get_queryset(self):
        return Estudiante.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'G-Profesor'
        context['object_list'] = Estudiante.objects.all()
        return context