from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Timestamp(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        abstract = True


class Auditable(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name="Кто создал",
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        blank=True,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        verbose_name="Кто изменил",
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class Product(Timestamp):
    title = models.CharField(verbose_name='Название', max_length=200, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
