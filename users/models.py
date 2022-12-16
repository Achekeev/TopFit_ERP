from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import CustomUserManager


STAFF_CHOICES = (
    ('Trainer', 'Тренер'),
    ('Manager', 'Менеджер'),
    ('Accountant', 'Бухгалтер'),
    ('Client', 'Клиент'),
)


class CustomUser(AbstractUser):
    login = models.CharField(max_length=50, verbose_name='Логин')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    passport_scan = models.ImageField(upload_to='media/', verbose_name='Скан паспорта')
    position = models.CharField(choices=STAFF_CHOICES, max_length=10)
    percent = models.IntegerField(default=0, verbose_name='Процент')
    salary = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Оклад', default=0)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'

    def __str__(self) -> str:
        return self.username
    

class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name='название филиала')
    address = models.CharField(max_length=255, verbose_name='Адрес Филиала')
    cashbox = models.DecimalField(decimal_places=2, default=0, verbose_name='Касса', max_length=20, max_digits=50)
    outcome = models.DecimalField(decimal_places=2, default=0, verbose_name='Расходы', max_length=20, max_digits=50)
    income = models.DecimalField(decimal_places=2, default=0, verbose_name='Доход', max_length=20, max_digits=50)

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название Группы')
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Тренер')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


# class Client(models.Model):
#     first_name = models.CharField(max_length=50, verbose_name='Имя')
#     last_name = models.CharField(max_length=50, verbose_name='Фамилия')
#     phone_number = models.CharField(max_length=50, verbose_name='Номер Телефона')
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
#
#     class Meta:
#         verbose_name = 'Клиент'
#         verbose_name_plural = 'Клиенты'
#
#     def __str__(self) -> str:
#         return self.last_name
