from django import forms
from django.core.validators import RegexValidator
from django.forms import CheckboxInput

from .models import *

textValidator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Поле должно содержать символы")
tagsValidator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Tags should contain letters")
passwordValidator = RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                                   "Пароль должен содержать минимум 8 символов, 1 букву и 1 цифру как минимум ")


class UserSignUpForm(forms.Form):
    first_name = forms.CharField(validators=[textValidator],
                                 label="Имя",
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'minlength': 2,
                                                               'maxlength': 30,
                                                               'placeholder': 'Имя'}))
    last_name = forms.CharField(validators=[textValidator],
                                label="Фамилия",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'minlength': 2,
                                                              'maxlength': 30,
                                                              'placeholder': 'Фамилия'}))
    username = forms.CharField(validators=[textValidator],
                               label="Никнейм",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'minlength': 5,
                                                             'maxlength': 30,
                                                             'placeholder': 'Никнейм'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))
    password = forms.CharField(validators=[passwordValidator],
                               label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Пароль'}))
    password_confirmation = forms.CharField(label="Потверждение пароля",
                                            widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Подтверждение пароля'}))
    phoneNumber = forms.CharField(label="Номер телефона ")


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    comments = forms.CharField(required=True)
