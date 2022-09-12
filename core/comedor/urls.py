from django.urls import path
from core.comedor.views.listas_usu.views import *
from core.comedor.views.reportes.views import *
from core.comedor.views.profesor_views.views import *
from core.comedor.views.Cocina_Views.Views import *
app_name = 'comedor'

urlpatterns = [
    #ADMIN
    path('gestionUsuarios/listados',listaUsersView.as_view(), name = 'ListUsu'),
    path('general/',admPrincipalView.as_view(), name = 'AdmGeneral'),
    path('ReporteProduccion/',listadoReportes.as_view(), name = 'admRepProd'),
    path('cronograma/',admCrono.as_view(), name = 'admCrono'),
    #PROFESOR
    path('listadosUsc/', ListaCreateView.as_view()  , name = 'listasUsc'),

    #Cocinero
    path('produccionCocina/', ProduccionCreateView.as_view(), name='CocinaProd'),
    path('desperdiciosCocina/', DesperdiciosCreateView.as_view(), name='CocinaDesp'),
]