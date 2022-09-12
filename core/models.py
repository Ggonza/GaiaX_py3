from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    usu_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usu_creation',
                                     null=True, blank=True)
    usu_actualiza = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usu_update',
                                       null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_actualiza = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class DespBaseModel(models.Model):
    usu_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usu_Despcreation',
                                     null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
