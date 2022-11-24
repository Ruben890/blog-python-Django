from django.contrib.auth.models import User

from django.db.models.signals import post_save
from .models import profile

from django.dispatch import receiver


# ? aqui estoy creadon un perfil señal es desir que cuando cree un

# ? nuevo ususraio automaticamente se creeara un perfil nuevo

#! https://docs.djangoproject.com/en/4.1/ref/signals/


@receiver(post_save, sender=User)
def crear_perfiles(sender, instance, created, **kwargs):

    if created:
        profile.objects.create(user=instance)
