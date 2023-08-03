from django import forms
from products import models


class Categorycreate(forms.Form):
    title = forms.CharField(max_length=200)


class Productcreate(forms.Form):
    img = forms.ImageField(required=False)
    title = forms.CharField(max_length=24)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
    category = forms.ModelChoiceField(queryset=models.Category.objects.all())
    prize = forms.FloatField()
    phone_number = forms.FloatField()


class CommentsCreateForm(forms.Form):
    text = forms.CharField(max_length=355)


class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
