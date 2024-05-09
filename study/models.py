from django.db import models

# Create your models here.
class Studyes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Аты жону')
    age = models.IntegerField(verbose_name='Жашы')
    school = models.CharField(max_length=255, verbose_name='Мектеби')
    address = models.CharField(max_length=255, verbose_name='Адресс')
    phone = models.CharField(max_length=255, verbose_name='телефон')
    email = models.EmailField(verbose_name='почта')
    price = models.DecimalField(verbose_name='Акчасы', max_digits=5, decimal_places=3)

    def __str__(self):
        return self.name