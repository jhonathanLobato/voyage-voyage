from django.urls import path
#importando as views de views de app
from voyage.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name="login"),
    path('blog/', blog, name='blog'),
    path('blog_pagina/<int:foto_id>', blog_pagina, name="blog_pagina"),
]
