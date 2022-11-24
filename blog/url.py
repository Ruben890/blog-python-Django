from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePage, name="blog"),
    path('Juegos', Juego, name="juegos"),
    path('Noticias', Noticias, name="Noticias"),
    path('Tegnologia', Tecnología, name="Tecnología"),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logaud', Logaud.as_view(), name='logaud'),
    path('AgregarPost', CreatePost.as_view(), name='AgregarPost'),
    path('Editar_perfil/<int:pk>/',
         EditarImagenDePerfil.as_view(), name='Editar_perfil'),
    path('verPost', VerMisPost.as_view(), name='verPost'),
    path('Eliminar/<int:id>', Eliminar, name='Eliminar'),
    path('Comentarios/<int:pk>', Comentario.as_view(), name='Comentarios'),
    path('EliminarComentarios/<int:id>', EliminarComentario, name='EliminarComentarios'),
    path('Editar/<int:pk>', Editar.as_view(), name='Editar'),
    path('Perfil/<str:username>', VerPerfil.as_view(), name='Perfil')

]
