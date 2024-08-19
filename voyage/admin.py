from django.contrib import admin
from voyage.models import blog_post

class Posts_lista(admin.ModelAdmin):
    list_display = ("id", "titulo")
    list_display_links = ("id", "titulo")

admin.site.register(blog_post, Posts_lista)