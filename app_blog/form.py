from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class User_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

class Ranking_form(forms.Form):
    name_course = forms.CharField(max_length=40) 
    opinion = forms.CharField()
    score = forms.IntegerField(min_value=1, max_value=10)
    id_number = forms.IntegerField()

class Post_form(forms.Form):
    title = forms.CharField(max_length=40) 
    text = forms.CharField()
    id_number = forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Nombre', min_length=8, max_length=12)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}