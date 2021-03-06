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
