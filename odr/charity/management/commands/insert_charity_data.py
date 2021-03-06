from django.core.management import BaseCommand

from charity.management.commands_data.charity_data import CATEGORY_DATA
from charity.models import Category


def insert_category():
    for name in CATEGORY_DATA:
        Category.objects.create(name=name)

