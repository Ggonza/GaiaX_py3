from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    imagen = models.ImageField(upload_to='users%y%m%d', null=True, blank=True )

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL,'img/empty.jpg')


