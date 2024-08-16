from django.shortcuts import render

def index(request):
    return render(request, 'voyage/index.html')

def login(request):
    return render(request, 'voyage/login.html')

# Blogs
def blog(request):
    return render(request, 'voyage/blog/blog.html')

def blog_pagina(request):
    return render(request, 'voyage/blog/pagina_blog.html')

def criar_pagina(request):
    return render(request, 'criar_pagina.html')