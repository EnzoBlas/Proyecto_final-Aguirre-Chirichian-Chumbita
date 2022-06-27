from django.contrib import admin
from .models import Post, Userpost, Ranking, Comment, Message, Avatar

# Register your models here.


admin.site.register(Post)
admin.site.register(Ranking)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Avatar)

