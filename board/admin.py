from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Subforum)
class SubforumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["forum_name"]}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Reply)