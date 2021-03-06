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
