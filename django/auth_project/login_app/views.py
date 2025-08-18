from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
# from django.contrib.messages import get_messages


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_user = request.POST.get('remember_user')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                request.session["last_login"] = datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S'
                )
                if remember_user:
                    request.session.set_expiry(2592000)
                else:
                    request.session.set_expiry(3600)

                messages.add_message(
                    request, messages.SUCCESS, "You're now logged in."
                )
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.add_message(
                    request, messages.WARNING, 'Account not active'
                )
                return render(request, 'login_app/login.html')
        else:
            messages.add_message(
                    request, messages.WARNING, 'Invalid login details'
                )
            return render(request, 'login_app/login.html')
    else:
        return render(request, 'login_app/login.html')


def special(request):
    return render(request, 'login_app/special.html')


def dashboard(request):
    last_login = request.session.get("last_login", False)
    my_dict = {'last_login': last_login}
    return render(request, 'login_app/dashboard.html', context=my_dict)
