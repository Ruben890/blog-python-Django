from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PostBLog, profile, Cometarios
from .choice import tipo


class UserRegister(UserCreationForm):
    email = forms.EmailField(
        label="Email", required=True)
    password1 = forms.CharField(
        label='Password', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email',  'username', 'password1', 'password2']
        # *esto remuve todo el texto del registro
        help_texts = {k: "" for k in fields}


class Post(forms.ModelForm):
    title = forms.CharField(label="Titulo", max_length=50, required=True,
                            widget=forms.TextInput())
    descriction = forms.Textarea()
    img = forms.ImageField(label="Imagen",
                           required=False, widget=forms.FileInput(attrs={'class': 'imagen'}))
    tipo = forms.ChoiceField(label='Tipo', required=True, choices=tipo)

    class Meta:
        model = PostBLog
        fields = ['title', 'descriction', 'img', 'tipo', 'complete']


class FormComentarios(forms.ModelForm):
    comentario = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder':'Agregar un Comentario'}
    ))

    class Meta:
        model = Cometarios
        fields = ['comentario']
