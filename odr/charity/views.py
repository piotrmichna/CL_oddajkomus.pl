from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from charity.models import Donation, Institution


class LandingPageView(View):
    """STRONA GŁÓWNA - KRÓTKI OPIS PRZEZNACZENIA"""

    def get(self, request):
        quantity = Donation.objects.all().aggregate(Sum('quantity'))
        donation = Institution.objects.count()
        fund = Institution.objects.filter(type=0)[:4]
        if len(fund) == 0:
            fund = None
        orgs = Institution.objects.filter(type=1)[:4]
        if len(orgs) == 0:
            orgs = None
        locales = Institution.objects.filter(type=2)[:4]
        if len(locales) == 0:
            locales = None
        return render(request, 'landing_page.html', {'quantity': quantity,
                                                     'donation': donation,
                                                     'fund': fund,
                                                     'orgs': orgs,
                                                     'locales': locales})


class AddDonationPageViev(View):
    """STRONA FORMULARZA DODAWANIA DAROWIZN"""

    def get(self, request):
        return render(request, 'donation_add.html')


class LoginView(View):
    """STRONA FORMULARZA LOGOWANIA"""

    def get(self, request):
        return render(request, 'login.html')


class RegistrationView(View):
    """STRONA FORMULARZA REJESTRACJI"""

    def get(self, request):
        return render(request, 'register.html')
