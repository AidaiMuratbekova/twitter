from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"
class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class RegisterView(TemplateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("successful-registration")

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)

class SuccessRegistrationView(View):
    template_name = "registration/success.html"
    def  get(self, request):
        return render(request, 'registration/success.html', {})