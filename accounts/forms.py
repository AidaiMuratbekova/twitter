from django import  forms
from django.contrib.auth import  get_user_model

from account.utils import send_activation_mail

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, required=True,widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=6, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','password','password_confirm','name','last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise  forms.ValidationError('Пользователь с таким email уже есть')
        return  email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self):
        user = User.objects.create(**self.cleaned_data)
        user.create_activation_code()
        send_activation_mail(user.email, user.activation_code)
        return user