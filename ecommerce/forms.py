# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Product, Brand, Order, Category, Discount, ProductComment


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Логін"
        self.fields['username'].help_text = ""
        self.fields['password'].label = 'Пароль'
        self.fields['password_check'].label = 'Повторіть пароль'
        self.fields['first_name'].label = "Ім'я"
        self.fields['last_name'].label = 'Прізвище'
        self.fields['email'].label = 'Електронна адреса'

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                {'username': 'Такий логін уже зареєстрований!'}, code='user exists')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                {'email': 'Така пошта вже зареєстрована!'}, code='email exists')
        if password != password_check:
            raise forms.ValidationError(
                {'password_check': 'Паролі не співпадають!'}, code='passwords do not match')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логін'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                {'username': 'Такого логіна не існує!'}, code='user does not exist')

        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError(
                {'password': 'Пароль неправильний!'}, code='password does not exist')


class OrderForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    phone = forms.CharField()
    delivery_type = forms.ChoiceField(widget=forms.Select(), choices=(
        [("self", "Самовивіз"), ("delivery", "Доставка")]))
    date = forms.DateField(
        widget=forms.SelectDateWidget(), initial=timezone.now())
    address = forms.CharField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Ваше ім'я"
        self.fields['surname'].label = 'Ваше прізвище'
        self.fields['phone'].label = 'Номер телефону'
        self.fields['phone'].help_text = "Будь ласка, вкажіть реальний номер, щоб з вами могли зв'язатися"
        self.fields['delivery_type'].label = 'Спосіб отримання'
        self.fields['address'].label = 'Адреса доставки'
        self.fields['address'].help_text = 'Вкажіть місто, вулицю, номер будинку (та квартири)'
        self.fields['comment'].label = 'Коментар до замовлення'
        self.fields['date'].label = 'Дата доставки'
        self.fields['date'].help_text = 'Доставка здійснюється впродовж 2-5 днів після оформлення замовлення.'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'slug', 'description',
                  'price', 'image', 'is_available']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['name']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'slug']


class AlterOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class DiscountForm(forms.ModelForm):

    class Meta:
        model = Discount
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = ProductComment
        fields = ['comment']
