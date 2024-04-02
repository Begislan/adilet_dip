from django.db import models

class Cisharp(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название темы")
    text = models.TextField(verbose_name="Данные")
    date = models.DateTimeField(verbose_name="Дата")

    def __str__(self):
        return self.title