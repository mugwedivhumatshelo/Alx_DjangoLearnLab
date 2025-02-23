from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if get_user_model().objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif get_user_model().objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                user = get_user_model().objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                messages.success(request, "You have successfully registered.")
                return redirect('list_books')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'register.html')

