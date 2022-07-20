from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auth_app.forms import SchoolUserLoginForm, SchoolUserRegisterForm, SchoolUserEditForm
from auth_app.models import SchoolUser


def login(request):
    login_form = SchoolUserLoginForm(data=request.POST)
    next_url = request.GET.get('next', '')

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])

        return HttpResponseRedirect(reverse('home'))

    context = {
        'login_form': login_form,
        'next': next_url,
    }
    return render(request, 'auth_app/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def edit(request):
    if request.method == 'POST':
        edit_form = SchoolUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth_app:edit'))

    else:
        edit_form = SchoolUserEditForm(instance=request.user)

    context = {
        'edit_form': edit_form,
    }
    return render(request, 'auth_app/edit.html', context)


def register(request):
    if request.method == 'POST':
        register_form = SchoolUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth_app:login'))

    else:
        register_form = SchoolUserRegisterForm()

    context = {
        'register_form': register_form
    }
    return render(request, 'auth_app/register.html', context)
