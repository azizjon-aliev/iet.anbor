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
    
    
class Counterparty(models.Model):
    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрегенты'
        
    
    name = models.CharField(verbose_name='Наиминование', max_length=200, unique=True)
    full_name = models.CharField(verbose_name='Полное наиминование', max_length=200, unique=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=200, unique=True)
    inn = models.CharField(verbose_name='ИНН', max_length=200, unique=True)
    created_at = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
 
    def __str__(self) -> str:
        return self.full_name


class OperationGroup(models.Model):
    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
    
    class Status(models.IntegerChoices):
        INACTIVE = 0, "На расмотрения"
        ACTIVE = 1, "Принята"
    
    class Action(models.IntegerChoices):
        DEBIT = 0, "Расход"
        CREDIT = 1, "Приход"
        
    counterparty = models.ForeignKey(verbose_name='Контрагент', to=Counterparty, on_delete=models.CASCADE)
    action = models.SmallIntegerField(verbose_name='Действие', choices=Action.choices)
    status = models.SmallIntegerField(verbose_name='Статус', choices=Status.choices, default=Status.INACTIVE)
    comment = models.TextField(verbose_name='Комментарие', blank=True)
    created_at = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    
    def __str__(self) -> str:
        return self.counterparty.name
    

class Operation(models.Model):
    class Meta:
        verbose_name = 'Группа Операция'
        verbose_name_plural = 'Группа Операции'
        
    product = models.ForeignKey(verbose_name='Продукт', to=Product, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Ценна')
    discount = models.FloatField(verbose_name='Скыдка')
    group = models.ForeignKey(verbose_name='Группа', to=OperationGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    
    def __str__(self) -> str:
        return self.product.title