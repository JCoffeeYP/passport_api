from django.core.exceptions import ValidationError
from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=255,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=255,
                                 verbose_name='Фамилия')
    email = models.EmailField(max_length=255,
                              unique=True,
                              verbose_name='email')
    photo = models.ImageField(upload_to='photo/',
                              verbose_name='Фотография')

    class Meta:
        ordering = ['email', ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.email


class Passport(models.Model):
    number = models.CharField(max_length=10,
                              verbose_name='Номер паспорта',
                              unique=True)
    country = models.CharField(max_length=255,
                               verbose_name='Страна')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    expiration_date = models.DateField(verbose_name='Дата окончания')
    owner = models.ForeignKey(Account,
                              related_name='passports',
                              on_delete=models.CASCADE,
                              verbose_name='Владелец паспорта')

    class Meta:
        ordering = ['number', ]
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

    def __str__(self) -> str:
        return self.number

    def clean(self) -> None:
        if self.date_of_issue >= self.expiration_date:
            raise ValidationError(
                {'date_of_issue': ('Дата окончания действия паспорта должна '
                                   'быть позже даты выдачи паспорта')}
            )
