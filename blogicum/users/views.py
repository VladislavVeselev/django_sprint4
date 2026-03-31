from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'users/registration.html', {'form': form})