from django.core.management import BaseCommand

from charity.management.commands_data.charity_data import CATEGORY_DATA, INSTITUTION_DATA, DONATION_DATA
from charity.models import Category, Institution, Donation


def insert_category():
    for name in CATEGORY_DATA:
        Category.objects.create(name=name)


def insert_institutions():
    for name, description, type, categories in INSTITUTION_DATA:
        inst = Institution.objects.create(name=name, description=description, type=type)
        for catid in categories:
            inst.categories.add(Category.objects.get(id=catid))
        inst.save()


def insert_donation():
    for quantity, categories, institution, address, phone, city, zip, pick_date, pick_time, comment in DONATION_DATA:
        inst = Institution.objects.get(id=institution)
        donat = Donation.objects.create(quantity=quantity,
                                        institution=inst,
                                        address=address,
                                        phone_number=phone,
                                        city=city,
                                        zip_code=zip,
                                        pick_up_date=pick_date,
                                        pick_up_time=pick_time,
                                        pick_up_comment=comment)
        for catid in categories:
            donat.categories.add(Category.objects.get(id=catid))
        donat.save()


class Command(BaseCommand):
    help = 'Wstawienie danych dobroczynnośći do bazy.'

    def handle(self, *args, **options):
        insert_category()
        insert_institutions()
        insert_donation()
        print('Pomyślnie dodano testowe dane do bazy.')
