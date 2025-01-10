from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after sign-up
            return redirect('home')  # Redirect to home after successful sign-up
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('home')  # Redirect to home page or any page you prefer
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page or login page

