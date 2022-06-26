from datetime import date, datetime
from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from datetime import datetime

from app_blog.models import Post,Userpost,Ranking
from app_blog.form import User_form,Post_form,RankingForm,UserRegisterForm


def index(request):
    posts = Post.objects.all()

    context_dict = {
        'posts': posts
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )


def posts(request):
    posts = Post.objects.all()

    context_dict = {
        'posts': posts
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )



@login_required
def post_form(request):
    if request.method == 'POST':
        post_form = Post_form(request.POST)
        if post_form.is_valid():
            data = post_form.cleaned_data
            data_author=(str(Userpost.objects.filter(pk__contains=data['id_number']))[22:-3])
            post = Post(
                title=data['title'],
                text=data['text'],
                author=data_author
                )
            post.save()

            posts = Post.objects.all()
            context_dict = {
                'posts': posts
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/home.html"
            )

    post_form = Post_form(request.POST)
    context_dict = {
        'post_form': post_form
     }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/post_form.html'
    )


def ranking(request):
    return render(
        request=request,
        template_name="app_blog/ranking.html"
    )


def search(request):
    return render(request, "app_blog/search.html")

def search_post(request):
    context_dict = dict()
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(title__contains=search_param)
        query.add(Q(text__contains=search_param), Q.OR)
        posts = Post.objects.filter(query)
        context_dict = {
            'posts': posts
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/search.html",
    )
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class RankingListView(ListView):
    model = Ranking
    template_name = "app_blog/ranking_list.html"

class RankingDetailView(DetailView):
    model = Ranking
    template_name = "app_blog/ranking_detail.html"

class RankingCreateView(LoginRequiredMixin, CreateView):
    model = Ranking
    success_url = reverse_lazy('app_blog:ranking_list')
    fields = ['name_course', 'opinion', 'score']
  
class RankingUpdateView(LoginRequiredMixin, UpdateView):
    model = Ranking
    success_url = reverse_lazy('app_ranking:ranking-list')
    fields = ['name_course', 'opinion', 'score']

class RankingDeleteView(LoginRequiredMixin, DeleteView):
    model = Ranking
    success_url = reverse_lazy('app_coder:Ranking-list')

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = "app_blog/home.html"
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
            context_dict = {}
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/created_user.html",
            )
        else:
            status=[1]

    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form, "status": status},
        template_name="app_blog/register.html",
    )