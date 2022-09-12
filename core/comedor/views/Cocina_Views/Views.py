import datetime
from datetime import timedelta

from crum import get_current_user
from django.utils import timezone

from django.contrib.auth import login
from django.contrib.messages import success
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, FormView

from django.shortcuts import render, redirect
from django.db import connection
from django.db.models import Sum
from core.comedor.forms import PesoProdForm, ListasUsuForm, pesoDesperdicios
from core.comedor.models import Cocinero, ListaUsc, Menu, PesoProd, Produccion, Desperdicios


class ProduccionCreateView(CreateView):
    model = Menu, PesoProd, Produccion
    form_class = PesoProdForm
    template_name = 'Cocinero/Cocina_P.html'
    success_url = reverse_lazy('comedor:CocinaProd')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'G-Cocina'
        query = ListaUsc.objects.filter(fecha__gte=timezone.now() - timedelta(1)).aggregate(Sum('cantidad_est')).values()
        context['cantSs'] = query
        context['menu'] = Menu.objects.all()
        return context

    def form_valid(self, form):
        cant_est = ListaUsc.objects.filter(fecha__gte=timezone.now() - timedelta(1)).aggregate(Sum('cantidad_est'))
        #Guardar Formulario
        form.save()

        user = get_current_user()
        print('user>>> ',user)
        if user is not None:
                print('Entro el user ', user)
                peso = PesoProd.objects.latest('id_pesoprod')
                regPeso = Produccion.objects.create(cant_est=cant_est['cantidad_est__sum'],
                                                    peso_prod_id_pesoprod=peso,
                                                    usu_creacion=user)
        #Guardar Form Regis Peso
                regPeso.save()
        return redirect(self.success_url)



class DesperdiciosCreateView(CreateView):
    model = Desperdicios
    form_class = pesoDesperdicios
    template_name = 'Cocinero/desperdicios/Desperdicios.html'
    success_url = reverse_lazy('comedor:CocinaDesp')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'G-Cocina'
        return context


    def form_valid(self, form):

        user = get_current_user()
        if user is not None:
                print('Entro el user ', user)
                regPeso = Desperdicios.objects.create(usu_creacion_id=user.pk)
        #Guardar Form Regis Peso
                regPeso.save()
                form.save()
        return redirect(self.success_url)
