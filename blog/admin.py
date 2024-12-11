from django.contrib import admin

# Register your models here.
from .models import BlogPost


#Django管理サイトにBlogPostを登録する
admin.site.register(BlogPost)