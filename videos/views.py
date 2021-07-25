from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm
from .models import UserProfile
from django.core.paginator import Paginator


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
    """ Displays the user profile"""
    if request.method == 'POST': 
         
        video = request.FILES['video']
        print(video)
        teacher_profile = UserProfile.objects.get(user_id=request.user.id)
        teacher_profile.video = video

        teacher_profile.save()

        return redirect('profile')
    else:
        return render(request, 'profile/home.html', {})


def teacher_listing(request):
    """Show all the available Teachers"""
    teacher_list = UserProfile.objects.get_queryset().order_by('id')
    paginator = Paginator(teacher_list, 10) # Show 10 jobs per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'teachers/home.html', {'page_obj': page_obj})