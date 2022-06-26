from app_blog import views
from django.urls import path
from django.contrib import admin

app_name ='app_blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('login/', views.login_request, name='user-login'),
    path('logout/', views.logout_request, name='user-logout'),
    path('post_add/', views.post_create, name='post-add'),
    path('post_list/', views.PostListView.as_view(), name='post-list'),
    path('post_search/', views.post_search, name='post_search'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('ranking_add/', views.ranking_create, name='ranking-add'),
    path('ranking_list/', views.RankingListView.as_view(), name='ranking-list'),
    path('ranking_search/', views.ranking_search, name='ranking_search'),
    path('ranking/<int:pk>/detail', views.RankingDetailView.as_view(), name='ranking-detail'),
    path('ranking/<int:pk>/update', views.RankingUpdateView.as_view(), name='ranking-update'),
    path('ranking/<int:pk>/delete', views.RankingDeleteView.as_view(), name='ranking-delete'),
    path('register', views.register, name='user-register'),
]