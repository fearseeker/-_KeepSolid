from django import forms
from django.contrib.auth import authenticate
from .models import Account


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data

    def save(self, commit=True):
        user = Account.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(username=email, password=password)

        if not user:
            raise forms.ValidationError("Неверный email или пароль")

        self.user = user
        return cleaned_data