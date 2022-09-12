from django.contrib import admin
from django.urls import path, include
from core.login.views import loginFormView, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', loginFormView.as_view(), name = ''),
    path('', include('core.login.urls'), name = 'login'),
    path('', logout_view, name = 'logout'),
    path('comedor/', include('core.comedor.urls'), name = 'comedor'),
]
