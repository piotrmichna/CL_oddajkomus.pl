from charity.management.commands_data.charity_data import CATEGORY_DATA, INSTITUTION_DATA
from charity.models import Category, Institution


def insert_category():
    for name in CATEGORY_DATA:
        Category.objects.create(name=name)


def insert_institutions():
    for name, description, type, categories in INSTITUTION_DATA:
        inst = Institution.objects.create(name=name, description=description, type=type)
        for catid in categories:
            inst.categories.add(Category.objects.get(id=catid))
        inst.save()
