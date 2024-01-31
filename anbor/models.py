from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    name = models.CharField(verbose_name='Название', max_length=200, unique=True, db_index=True)
    creadet_at = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновление', auto_now=True)