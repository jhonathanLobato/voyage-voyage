from django.urls import path, include
#importando as views de views de app
from voyage.views import index

urlpatterns = [
    path('', index, name='index')
]
