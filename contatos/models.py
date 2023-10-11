from django.db import models

# Create your models here.


class Amigo(models.Model):
    Titulo = models.CharField("Título", max_length=200, blank=True)
    Artista = models.CharField("Artista", max_length=200, blank=True)
    Ano = models.DateField("Ano de Lançamento", blank=True, null=True)
    Capa = models.ImageField("Capa", upload_to="avatares", blank=True, null=True)
    Duraçao = models.CharField("Duraçao", max_length=200, blank=True)
    
    def __str__(self):
        return self.Titulo
