from django.db import models

class Java(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название", default="test")
    text = models.TextField(verbose_name="Данные")
    date = models.DateTimeField(verbose_name="Дата")

    def __str__(self):
        return self.title