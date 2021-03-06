from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    """STRONA GŁÓWNA - KRÓTKI OPIS PRZEZNACZENIA"""

    def get(self, request):
        return render(request, 'landing_page.html')


class AddDonationPageViev(View):
    """STRONA FORMULARZA DODAWANIA DAROWIZN"""

    def get(self, request):
        return render(request, 'donation_add.html')


class LoginView(View):
    """STRONA FORMULARZA LOGOWANIA"""

    def get(self, request):
        return render(request, 'login.html')
