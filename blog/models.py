from django.db import models
from django.contrib.auth.models import User
from .choice import tipo
from django.utils import timezone


class profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='perfil')
    image = models.ImageField(default='buo.jpg')

    def __str__(self):
        return self.user.username

# * agregar nuevo post a la base de datos


class PostBLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='Posts')
    title = models.CharField('Title', max_length=50, null=False, blank=False)
    descriction = models.TextField('Descripsion', null=False, blank=False)
    img = models.ImageField('Imagen',
                            max_length=150, upload_to='img', null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(choices=tipo, max_length=50,
                            null=False, blank=False)
    complete = models.BooleanField('completado', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['data']

# * Agregar Comentarios


class Cometarios(models.Model):
    comentario = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comentario')
    post = models.ForeignKey('PostBLog', on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['data']
