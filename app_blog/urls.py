from app_blog import views
from django.urls import path
from django.contrib import admin

app_name ='app_blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('login/', views.login_request, name='user-login'),
    path('logout/', views.logout_request, name='user-logout'),
    path("posts/", views.posts, name="posts"),
    path("post-form", views.post_form, name="post_form"),
    path('ranking_add/', views.RankingCreateView.as_view(), name='ranking_add'),
    path('ranking_list/', views.RankingListView.as_view(), name='ranking_list'),
    path('ranking/<int:pk>/detail', views.RankingDetailView.as_view(), name='ranking_detail'),
    path('ranking/<int:pk>/update', views.RankingUpdateView.as_view(), name='ranking_update'),
    path('ranking/<int:pk>/delete', views.RankingDeleteView.as_view(), name='ranking_delete'),
    path('register', views.register, name='user-register'),
    path('search_post/', views.search_post, name='search_post'),
    path('search/', views.search),

]