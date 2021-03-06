from django.contrib.auth.models import User
from django.db import models

TYPE_INSTITUT = [
    (0, "fundacja"),
    (1, "organizacja pozarządowa"),
    (2, "zbiórka lokalna"),
]


class Category(models.Model):
    name = models.CharField(max_length=128, null=False, verbose_name='Kategoria')

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=128, null=False, verbose_name='Kategoria')
    description = models.TextField(max_length=512, null=True, verbose_name='Opis')
    type = models.SmallIntegerField(choices=TYPE_INSTITUT, default=0, verbose_name='Typ')
    categories = models.ManyToManyField(Category, verbose_name='Kagegoria')

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.SmallIntegerField(null=False, verbose_name='Liczba worków')
    categories = models.ManyToManyField(Category, verbose_name='Kategoria')
    institution = models.ForeignKey(Institution, null=False, on_delete=models.CASCADE, verbose_name='Instytucja')
    address = models.CharField(max_length=128, null=False, verbose_name='Ulica i numer domu')
    phone_number = models.IntegerField(null=False, verbose_name='Telefon')
    city = models.CharField(max_length=32, null=False, verbose_name='Miasto')
    zip_code = models.CharField(max_length=6, null=False, verbose_name='Kod pocztowy')
    pick_up_date = models.DateField(null=False, verbose_name="Data odbioru")
    pick_up_time = models.TimeField(null=False, verbose_name="Godzina odbioru")
    pick_up_comment = models.CharField(max_length=192, verbose_name='Notatka do odbioru')
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, verbose_name='Urzytkownik')

    def __str__(self):
        return f'Darowizna [{self.id}]'
