from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    """STRONA GŁÓWNA - KRÓTKI OPIS PRZEZNACZENIA"""

    def get(self, request):
        return render(request, 'landing_page.html')
