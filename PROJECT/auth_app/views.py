from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from auth_app.forms import CustomUserCreationForm

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Wohoo! User Created")
            return redirect('login')
        messages.error(request, "Please Check the error !")
        
    form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form' : form})


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return HttpResponse("Logged in successfully!")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')