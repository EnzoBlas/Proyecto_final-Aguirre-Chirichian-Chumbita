from django.views.static import serve
from app_blog import views
from app_blog.views import error_404_view
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name ='app_blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('abouts/',views.aboutsView, name='abouts'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path("", views.index, name='home'),
    path('login/', views.login_request, name='user-login'),
    path('logout/', views.logout_request, name='user-logout'),
    path('post_add/', views.post_create, name='post-add'),
    path('post_list/', views.PostListView.as_view(), name='post-list'),
    path('post_search/', views.post_search, name='post_search'),
    path('post/<int:pk>/detail',views.comment_post, name='post-detail'),
    path('comment/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile, name='profile'),
    path('user_update/', views.user_update, name='user-update'),
    path('ranking_add/', views.ranking_create, name='ranking-add'),
    path('ranking_list/', views.RankingListView.as_view(), name='ranking-list'),
    path('ranking_search/', views.ranking_search, name='ranking_search'),
    path('ranking/<int:pk>/detail', views.comment_rank, name='ranking-detail'),
    path('ranking/<int:pk>/update', views.RankingUpdateView.as_view(), name='ranking-update'),
    path('ranking/<int:pk>/delete', views.RankingDeleteView.as_view(), name='ranking-delete'),
    path('message/', views.message_list, name='message-list'),
    path('message_add/', views.message_create, name='message-add'),
    path('admin_register', views.admin_register, name='admin-register'),
    path('register', views.register, name='user-register'),
]

from django.conf.urls import handler404
from django.conf.urls import handler500

handler404 = 'app_blog.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


