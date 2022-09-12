from django import forms
from django.forms import ModelForm
from core.comedor.models import ListaUsc, Menu, PesoProd, Desperdicios

class ListasUsuForm(ModelForm):
    class Meta:
        model = ListaUsc
        fields = ['cantidad_est']

class PesoProdForm(forms.ModelForm):
    class Meta:
        model = PesoProd
        fields = ['item1','item2','item3','item4','item5', 'menu_idmenu']


class pesoDesperdicios(forms.ModelForm):
    class Meta:
        model = Desperdicios
        fields = ['peso_solidos', 'peso_liquidos']
