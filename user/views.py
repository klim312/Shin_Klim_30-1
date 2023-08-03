from django.shortcuts import render, redirect
from user.form import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        context_data = {'form': RegisterForm}
        return render(request, 'user/register.html', context=context_data)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/user/login/')
            else:
                form.add_error('password1', "password is incorrect, please enter a valid password")
        return render(request, 'user/register.html', context={'form': form})


def login_view(request):
    if request.method == 'GET':
        context_data = {'form': login_view}
        return render(request, 'user/login.html', context=context_data)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user:
                login(request=request, user=user)
                return redirect('/products/')
