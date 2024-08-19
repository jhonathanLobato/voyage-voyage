from django.db import models

class blog_post(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=False, blank=False)
    imagem = models.CharField(max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def formatado_data(self):
        return f"{self.titulo}"