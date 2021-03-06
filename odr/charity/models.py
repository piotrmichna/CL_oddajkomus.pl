from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, null=False, verbose_name='Kategoria')

    def __str__(self):
        return self.name
