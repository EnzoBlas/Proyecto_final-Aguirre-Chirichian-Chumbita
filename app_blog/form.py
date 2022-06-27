from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_blog.models import Avatar

class RankingForm(forms.Form):
    name_course = forms.CharField(label='Nombre del curso', max_length=40) 
    opinion = forms.CharField(label='Comentario del curso', widget=forms.Textarea)
    score = forms.IntegerField(label='Nota del curso', min_value=1, max_value=10)

class PostForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=40) 
    content = forms.CharField(label='Contenido', widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre', min_length=3, max_length=12)
    last_name = forms.CharField(label='Apellido', min_length=3, max_length=12)
    username = forms.CharField(label='Usuario', min_length=8, max_length=12)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre', min_length=3, max_length=12)
    last_name = forms.CharField(label='Apellido', min_length=3, max_length=12)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image',)