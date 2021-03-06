from django.urls import path

from charity.views import (LandingPageView, AddDonationPageViev, LoginView, RegistrationView)

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing-page"),
    path('donation/add/', AddDonationPageViev.as_view(), name="donation-add"),
    path('login/', LoginView.as_view(), name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
]
