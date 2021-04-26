

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from operators.form import SignUpForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            user = User.objects.create(username=form.cleaned_data.get('email'))
            raw_password=user.set_password(raw_password=form.cleaned_data.get('password1', None))
            user.save()
           # username = form.cleaned_data.get('email')
            #raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def dashboard(request):
    return render(request, 'operators/dashboard.html')