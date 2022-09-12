from django.urls import path
from core.login.views import *
app_name = 'login'

urlpatterns = [
    path('',loginFormView.as_view(), name = 'loginUser'),
]