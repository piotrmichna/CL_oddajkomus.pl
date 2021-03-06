from django.urls import path

from charity.views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing-page"),
]