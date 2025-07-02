from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Signed in successfully!')
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'auth/signin.html', {'form': form})

def signout_view(request):
    logout(request)
    messages.success(request, 'Signed out successfully!')
    return redirect('signin')  