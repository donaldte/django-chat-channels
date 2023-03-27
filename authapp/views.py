from django.shortcuts import render, redirect
from .forms import SinUpForm

from django.contrib.auth import login


def signup(request):
    """ Vue de creation de compte """
    
    if request.method == "POST":
        form = SinUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
    else:
        form = SinUpForm()

    return render(request, 'auth/signup.html', {'form': form})            