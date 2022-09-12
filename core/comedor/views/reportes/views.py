import random
from django.http import request, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from core.comedor.models import UserUser, Profesor, Rector, Cocinero, Rol, Produccion, PesoProd
from django.views.generic import ListView, CreateView, TemplateView
from core.comedor.forms import ListasUsuForm
from django.contrib.auth.models import User


class listadoReportes(ListView):
    model = Cocinero,Produccion,PesoProd
    template_name = 'ReportesADM/REPproduccion.html'

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                pass
            else:
                data['error'] = 'ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)


    def get_queryset(self):
        return Produccion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gaia-Admin'
        context['cocinero'] = UserUser.objects.get(id=3)
        context['list_url'] = reverse_lazy('comedor:admRepProd')
        context['prod_list'] = Produccion.objects.all()
        return context