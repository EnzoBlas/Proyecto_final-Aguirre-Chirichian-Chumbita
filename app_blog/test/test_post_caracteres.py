from django.test import TestCase
import random
import string
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_blog.models import Post,Avatar
from app_blog.form import PostForm

# Create your tests here.

KEY_LEN = 20
char_list = [random.choice((string.ascii_letters + string.digits)) for _ in range(KEY_LEN)]
mock_name = ''.join(char_list)
print(f'----------> Prueba con: {mock_name}')

"""post = Post(
                    title=mock_name,
                    sub_title=data['sub_title'],
                    content=data['content'],  
                    author=request.user.username,
                    profile_picture=str(profile)[24:-3],
                    image_post = image
                    )"""
"""devuelve en el titulo de post caracteres aleatorios"""