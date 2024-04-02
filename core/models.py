from django.db import models

class Python(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название темы")
    text = models.TextField(verbose_name="Данные")
    date = models.DateTimeField(verbose_name="Дата темы")

    def __str__(self):
        return self.title