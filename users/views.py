from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm, UserPictureForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"{username}, your account has been successfully created! ")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        'title': 'Register Page',
        'form': form
    }

    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        i_form = UserPictureForm(request.POST, request.FILES, instance=request.user.profile)
        p_form = UserProfileForm(request.POST, instance=request.user)
        if i_form.is_valid() and p_form.is_valid():
            i_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect('users:profile')
    else:
        i_form = UserPictureForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)

    context = {
        'title': 'Profile Page',
        'i_form': i_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)