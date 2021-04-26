from django.conf.urls import url
from django.contrib.auth import views
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ProfilePage, RegisterView, SuccessRegistrationView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    url(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path('successful_registration/', SuccessRegistrationView.as_view(), name ="successful-registration"),

]
