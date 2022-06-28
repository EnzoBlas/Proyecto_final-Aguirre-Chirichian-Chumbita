import os
import re
import random
import string
from tkinter.tix import Form

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth import get_user_model

from app_blog.models import Post,Ranking,Comment,CommentRank,Avatar,Message
from app_blog.form import UserRegisterForm, PostForm, RankingForm, CommentForm, AvatarForm, UserEditForm, UserAdminForm


def get_avatar(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

def index(request):
    avatar = get_avatar(request)
    posts = Post.objects.all().order_by('-pk')[0:6]
    context_dict = {
        'posts': posts,
        **avatar
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )

def profile(request):
    avatar = get_avatar(request)
    print(avatar)
    if type(avatar) == None:
        context_dict ={}
    else:
        context_dict ={
           **avatar
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/profile.html",
    )

def post_search(request):
    context_dict = dict()
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(title__contains=search_param)
        query.add(Q(content__contains=search_param), Q.OR)
        posts = Post.objects.filter(query)
        context_dict = {
            'posts': posts
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/post_search.html",
    )

def ranking_search(request):
    context_dict = dict()
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name_course__contains=search_param)
        query.add(Q(opinion__contains=search_param), Q.OR)
        rankings = Ranking.objects.filter(query)
        context_dict = {
            'rankings': rankings
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/ranking_search.html",
    )

@login_required
def post_create(request):
    profile = Avatar.objects.filter(user=request.user.id)
    if Avatar.objects.filter(user=request.user.id).exists() == True:
        if request.method == 'POST':
            post_create = PostForm(request.POST, request.FILES)
            if post_create.is_valid():
                data = post_create.cleaned_data
                image = request.FILES.get('image_post')

                # Una pequeña muestra de procesos de unit test
                #KEY_LEN = 20
                #char_list = [random.choice((string.ascii_letters + string.digits)) for _ in range(KEY_LEN)]
                #mock_name = ''.join(char_list)
                #print(f'----------> Prueba con: {mock_name}')
                
                post = Post(
                    title=data['title'],
                    sub_title=data['sub_title'],
                    content=data['content'],  
                    author=request.user.username,
                    profile_picture=str(profile)[24:-3],
                    image_post = image
                    )

                post.save()

            context_dict = {}
            return redirect ("app_blog:post-list")

    else:
        context_dict = {}
        return redirect ("app_blog:avatar-load")

    post_form = PostForm(request.POST)
    context_dict = {
        'post_form': post_form,
     }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/post_form.html'
    )
    
@login_required
def comment_post(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    comment_create = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_create.is_valid():
            data    = comment_create.cleaned_data
            comment = Comment(
                author = request.user.username,
                text = data['content'],
                post_id = pk
                )
            
            comment.save()
            comments = Comment.objects.filter(post_id=pk)

            context_dict = {
                'comment_form': comment_create,
                'post'   : post,
                'comments' : comments
            }
            return render(
                request      =request,
                context      =context_dict,
                template_name="app_blog/post_detail.html"
            )

    
    context_dict = {
        'comment_form': comment_create,
        'comments'    : comments,
        'post'        : post 
     }
    return render(
        request      = request,
        context      = context_dict,
        template_name= 'app_blog/post_detail.html'
    )

@login_required
def ranking_create(request):
    profile = Avatar.objects.filter(user=request.user.id)
    if Avatar.objects.filter(user=request.user.id).exists() == True:
        if request.method == 'POST':
            ranking_create = RankingForm(request.POST)
            if ranking_create.is_valid():
                data = ranking_create.cleaned_data
                ranking = Ranking(
                    name_course=data['name_course'],
                    opinion=data['opinion'],
                    score=data['score'],
                    author=request.user.username,
                    profile_picture=str(profile)[24:-3]
                    )
                ranking.save()

            context_dict = {}
            return redirect ("app_blog:ranking-list")
    else: 
        context_dict = {}
        return redirect ("app_blog:avatar-load")


    ranking_form = RankingForm(request.POST)
    context_dict = {
        'ranking_form': ranking_form
     }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/ranking_form.html'
    )

@login_required
def message_create(request):
    profile = Avatar.objects.filter(user=request.user.id)
    if Avatar.objects.filter(user=request.user.id).exists() == True:
        if request.method == 'POST':
            print(request)
            message = Message(
                author=request.user.username,
                receiver=request.POST['selectReceiver'],
                text=request.POST['messsage_text'],
                profile_picture=str(profile)[24:-3]
                )
            message.save()

            messages = Message.objects.all()
            message_list = []
            for message in messages:
                if message.receiver == request.user.username:
                    message_list.append(message)
            context_dict = {
                'message_list': message_list
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/message_list.html"
            )
    else: 
        context_dict = {}
        return redirect ("app_blog:avatar-load")

    message_form = Message(request.POST)
    User = get_user_model()
    user_list = User.objects.all()
    print(user_list)
    context_dict = {
        'user_list': user_list,
        'message_form': message_form
     }

    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/message_form.html'
    )
@login_required
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        message_list = []
        for message in messages:
            if message.receiver == request.user.username:
                message_list.append(message)
        context_dict = {
            'message_list': message_list
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_blog/message_list.html"
        )


@login_required
def comment_rank(request,pk):
    ranking = Ranking.objects.get(pk=pk)
    comments = CommentRank.objects.filter(rank_id=pk)
    comment_create = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_create.is_valid():
            data    = comment_create.cleaned_data
            comment = CommentRank(
                author = request.user.username,
                text = data['content'],
                rank_id = pk
                )
            
            comment.save()
            comments = CommentRank.objects.filter(rank_id=pk)

            context_dict = {
                'comment_form': comment_create,
                'ranking'   : ranking,
                'comments' : comments
            }
            return render(
                request      =request,
                context      =context_dict,
                template_name="app_blog/ranking_detail.html"
            )

    
    context_dict = {
        'comment_form': comment_create,
        'comments'    : comments,
        'ranking'        : ranking 
     }
    return render(
        request      = request,
        context      = context_dict,
        template_name= 'app_blog/ranking_detail.html'
    )
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class RankingUpdateView(LoginRequiredMixin, UpdateView):
    model = Ranking
    success_url = reverse_lazy('app_blog:ranking-list')
    fields = ['name_course', 'opinion', 'score']

class RankingDeleteView(LoginRequiredMixin, DeleteView):
    model = Ranking
    success_url = reverse_lazy('app_blog:ranking-list')

class RankingListView(ListView):
    model = Ranking
    template_name = "app_blog/ranking-list.html"
    ordering = ['-pk']

class PostListView(ListView):
    model = Post
    template_name = "app_blog/post-list.html"
    ordering = ['-pk']

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app_blog/comment_form.html"
    model = Comment
    success_url = reverse_lazy('app_blog:post-list' )
    fields = ['text']

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('app_blog:post-list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app_blog/post_form.html"
    model = Post
    success_url = reverse_lazy('app_blog:post-list')
    fields = ['title', 'content']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('app_blog:post-list')

class MessagesListView(ListView):
    model = Message
    template_name = "app_blog/message-list.html"

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect

def login_request(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                avatar = get_avatar(request)
                template_name = "app_blog/home.html"
                context_dict = {
                'posts': posts,
                **avatar
                }
            return render(
            request=request,
            context=context_dict,
            template_name="app_blog/home.html",
            )
        else:
            template_name = "app_blog/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_blog/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("app_blog:home")

def register(request):
    status=None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("app_blog:avatar-load")
        else:
            status=[1]

    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form, "status": status},
        template_name="app_blog/register.html",
    )

def admin_register(request):
    status=None
    if request.method == 'POST':
        form = UserAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("app_blog:avatar-load")
        else:
            status=[1]

    form = UserAdminForm()
    return render(
        request=request,
        context={"form":form, "status": status},
        template_name="app_blog/register-admin.html",
    )


def aboutsView(request):

    return render(
        request=request,
        template_name="app_blog/abouts.html",
    )

@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return redirect('home')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="app_blog/user_form.html",
    )

@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('home')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form,},
        template_name="app_blog/avatar_form.html",
    )
