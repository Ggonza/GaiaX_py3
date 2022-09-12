import datetime
from datetime import timedelta
from django.utils import timezone

from django.test import TestCase
from GaiaX_py.wsgi import *

from core.comedor.models import *
from django.db.models import Sum

#query = PesoProd.objects.get(idpeso_prod=1).item1
#sumery =  ListaUsc.objects.get()
peso = ListaUsc.objects.get(profesor_idprofesor=1).profesor_idprofesor_id
# ListaUsc.objects.filter(fecha__range=(fezha,iniFezcha))
iniFezcha = datetime.datetime.now()
fezha= iniFezcha - timedelta(1)
# query = ListaUsc.objects.filter(fecha__gte=fezha - iniFezcha).aggregate(sum('cantidad_est'))
print('Hoy= ',iniFezcha)
print('Dia anterior= ',fezha)
print('resultado query',peso)


