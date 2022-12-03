from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.admin import User

from .models import PostBLog, profile, Cometarios
from .forms import UserRegister, Post, FormComentarios


def HomePage(request):
    search = request.GET.get('search')

    if search:
        post = PostBLog.objects.filter(
            Q(title__icontains=search) | Q(descriction__icontains=search)
        ).distinct()
    else:
        post = PostBLog.objects.filter(complete=True).order_by('-data')
        paginator = Paginator(post, 5)
        page = request.GET.get('page')
        post = paginator.get_page(page)

    return render(request, 'index.html', {'post': post, 'user': profile.objects.all(),
                                          'form': FormComentarios,
                                          'coment': Cometarios.objects.all().order_by('-data')})


# * vista de  todos las publicasiones refernetes a juegos
def Juego(request):
    search = request.GET.get('search')

    if search:
        post = PostBLog.objects.filter(
            Q(title__icontains=search) | Q(descriction__icontains=search)
        ).distinct()
    else:
        post = PostBLog.objects.filter(
            complete=True, tipo='juegos').order_by('-data')
        paginator = Paginator(post, 5)
        page = request.GET.get('page')
        post = paginator.get_page(page)

    return render(request, 'index.html', {'post': post, 'user': profile.objects.all(),
                                          'form': FormComentarios,
                                          'coment': Cometarios.objects.all().order_by('-data')})

# * vista de  todos las publicasiones refernetes a Noticias


def Noticias(request):
    search = request.GET.get('search')

    if search:
        post = PostBLog.objects.filter(
            Q(title__icontains=search) | Q(descriction__icontains=search)
        ).distinct()
    else:
        post = PostBLog.objects.filter(
            complete=True, tipo='Noticias').order_by('-data')
        paginator = Paginator(post, 5)
        page = request.GET.get('page')
        post = paginator.get_page(page)

    return render(request, 'index.html', {'post': post,
                                          'user': profile.objects.all(),
                                          'form': FormComentarios,
                                          'coment': Cometarios.objects.all().order_by('-data')})


# * vista de  todos las publicasiones refernetes a Tecnologias
def Tecnología(request):
    search = request.GET.get('search')
    if search:
        post = PostBLog.objects.filter(
            Q(title__icontains=search) | Q(descriction__icontains=search)
        ).distinct()
    else:
        post = PostBLog.objects.filter(
            complete=True, tipo='Tecnología').order_by('-data')
        paginator = Paginator(post, 5)
        page = request.GET.get('page')
        post = paginator.get_page(page)

    return render(request, 'index.html', {'post': post, 'user': profile.objects.all(),
                                          'form': FormComentarios,
                                          'coment': Cometarios.objects.all().order_by('-data')})


# *agregar nuevo post


class CreatePost(View):
    def get(self, request):
        form = Post
        return render(request, 'AgregarPost.html', {'form': form})

    def post(self, request):
        corrent_user = get_object_or_404(User, pk=request.user.pk)
        form = Post(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = corrent_user
            post.save()
        return redirect('blog')


# *agregar comentarios

class Comentario(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        post = PostBLog.objects.get(pk=pk)
        form = FormComentarios(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.author = user
            comentario.post = post
            comentario.save()
        return redirect('blog')

# *Cambiar imagen de perfil del usuario
# ? con sesto solo podras cambiar la imagen de perfil


class EditarImagenDePerfil(LoginRequiredMixin, UpdateView):
    model = profile
    fields = ['image']
    context_object_name = 'user'
    template_name = 'Cambiar_imagen_Perfil.html'
    success_url = reverse_lazy('blog')


# *ver los post que el ususuario al subido al blog
# ? aqui podras editar eliminar y ver todos las publicasiones o post que a publicado,
# ? el propietario de la cuenta

class VerMisPost(LoginRequiredMixin, View):
    def get(self, request):
        post = PostBLog.objects.all()
        perfil = profile.objects.all()
        user = User.objects.all()
        paginator = Paginator(post, 5)
        page = request.GET.get('page')
        post = paginator.get_page(page)
        context = {
            'post': post,
            'user': perfil
        }
        return render(request, 'VerPost.html', context)

# * Ver perfil de Usuario


class VerPerfil(View):
    def get(self, request, username, *args, **kwargs):
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            post = user.Posts.filter(complete=True).order_by('-data')
        else:
            post = current_user.Posts.filter(complete=True).order_by('-data')
            user = current_user

        return render(request, 'VerUser.html', {'user': user,
                                                'post': post,
                                                'perfil': profile.objects.all()})

# *eliminar post


@login_required
def Eliminar(request, id):
    post = PostBLog.objects.get(id=id)
    post.delete()
    return redirect('verPost')

# *eliminar Comentario


@login_required
def EliminarComentario(request, id):
    post = Cometarios.objects.get(id=id)
    post.delete()
    return redirect('blog')

#*editar comentarios
class EditarComentario(LoginRequiredMixin, UpdateView):
    model = PostBLog
    template_name = "AgregarPost.html"
    form_class = Post
    success_url = reverse_lazy('blog')

# *editar Post


class Editar(LoginRequiredMixin, UpdateView):
    model = PostBLog
    template_name = "AgregarPost.html"
    form_class = Post
    success_url = reverse_lazy('verPost')


# *login


class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog')

# * logaud


class Logaud(LogoutView):

    def get_success_url(self):
        return reverse_lazy('blog')

# * registro de ususarios


class Register(FormView):
    fields = '__all__'
    template_name = 'register.html'
    form_class = UserRegister
    redirect_authenticated_user = True
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
           return redirect('homepage')
        return super(Register, self).get(*args, **kwargs)
