from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = User.objects.all() 
    context = {
        'users': users
    }
    
    return render(request, 'users/user_list.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'users/profile.html', {'user': user})

def edit_profile(request):
    user_profile = request.user.profile  # Get the user's profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)  # Redirect to the profile view
    else:
        form = ProfileForm(instance=user_profile)
    
    return render(request, 'users/edit_profile.html', {'form': form})

def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile', username=username)

def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', username=username)
