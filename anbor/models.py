from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='Название', max_length=200, unique=True, db_index=True)
    created_at = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновление', auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    image = models.ImageField(verbose_name='Изоброжение', upload_to='products/', blank=True, null=True)
    title = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновление', auto_now=True)

    def __str__(self):
        return self.title
