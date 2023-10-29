from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pw = request.POST.get('password')
        pw2 = request.POST.get('password2')

        if pw != pw2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if len(username) < 4:
            messages.error(
                request, "Username must be at least 4 characters long")
            return redirect('register')

        if len(email) < 6:
            messages.error(request, "Email must be at least 6 characters long")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "You already exist brah :) ")
            return redirect('register')

        User.objects.create_user(
            username=username, email=email, password=paw)
        return redirect('login')

    return render(request, "registration/register.html")
