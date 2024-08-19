from django.shortcuts import render, get_object_or_404
from voyage.models import blog_post

def index(request):
    blogs = blog_post.objects.all()
    return render(request, 'voyage/index.html', {'blogs': blogs})

def login(request):
    return render(request, 'voyage/login.html')

# Blogs
def blog(request):
    post_preview = blog_post.objects.order_by("-data_criacao").all()
    post_id1 = 2
    post_id2 = 3
    post_id3 = 4
    post_destaque1 = get_object_or_404(blog_post, id=post_id1)
    post_destaque2 = get_object_or_404(blog_post, id=post_id2)
    post_destaque3 = get_object_or_404(blog_post, id=post_id3)
    return render(request, 'voyage/blog/blog.html', {'preview': post_preview, 'post_destaque1': post_destaque1, 'post_destaque2': post_destaque2, 'post_destaque3': post_destaque3})

def blog_pagina(request, foto_id):
    pagina = get_object_or_404(blog_post, pk=foto_id)
    return render(request, 'voyage/blog/pagina_blog.html', {'pagina': pagina})
