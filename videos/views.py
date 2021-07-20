from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm
from .models import UserProfile


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('User logged in!'))
            return redirect('home')
        else:
            messages.error(request, ('Error, cannot log in, please try again'))
            return redirect('login')
            
    else:
        return render(request, 'auth/login.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()

            # Favorite Color Challenge 

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            
            user_profile = form2.save(commit=False)
            user_profile.user = user
            user_profile.save() 
            form2.save_m2m()

            login(request, user)                                        # Built-up Django function to Login the User
            messages.success(request, ('You have been registered'))
            return redirect('home')
    else:
        form = SignUpForm()
        form2 = UserProfileForm()
        
    context = {'form': form, 'form2': form2,}
    return render(request, 'auth/register.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, ('User successfully Logged out!'))
    return redirect('home')


def profile_user(request):
    return render(request, 'profile/home.html', {})