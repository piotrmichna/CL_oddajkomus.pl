from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from charity.models import Donation, Institution


class LandingPageView(View):
    """STRONA GŁÓWNA - KRÓTKI OPIS PRZEZNACZENIA"""

    def get(self, request):
        quantity = Donation.objects.all().aggregate(Sum('quantity'))
        donation = Institution.objects.count()
        return render(request, 'landing_page.html', {'quantity': quantity, 'donation': donation})


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
