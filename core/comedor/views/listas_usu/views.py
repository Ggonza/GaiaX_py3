import random
from django.http import request
from django.shortcuts import render
from core.comedor.models import UserUser, Profesor, Rector, Cocinero, Rol
from django.views.generic import ListView, CreateView, TemplateView
from core.comedor.forms import ListasUsuForm
from django.contrib.auth.models import User

username = None


class admPrincipalView(TemplateView):
    model = UserUser
    template_name = 'admPrincipal/adminP.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gaia-Admin'
        return context


class listaUsersView(ListView):
    model = UserUser
    template_name = 'GestionUsu/listas.html'

    def get_queryset(self):
        return UserUser.objects.filter(rol_idrol=2)

    def get_context_data(self, **kwargs):
        rolvar = Rol.objects.get(idrol=2)
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gaia-Admin'
        context['roles'] =rolvar.rol_name
        return context

#sin uso
class listaUserCreateView(CreateView):
    model = UserUser
    form_class = ListasUsuForm
    template_name = 'GestionUsu/crear.html'


class admCrono(TemplateView):
    model = UserUser
    template_name = 'Cronograma/crono.html'