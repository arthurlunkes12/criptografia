from django.db import models


class TextoCriptografado(models.Model):
    texto_original = models.TextField()
    texto_criptografado = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
