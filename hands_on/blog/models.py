from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=100)
    temas = models.CharField(max_length=500)


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=20, default='auto_ajuda')
    autor = models.ForeignKey(Autor)
    autores = models.ManyToManyField(Autor,
                                     related_name="autores_id",
                                     null=True)
