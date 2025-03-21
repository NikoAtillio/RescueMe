from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('core:index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('core:index')

@login_required
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if not confirm:
            messages.error(request, 'You must confirm the deletion by checking the box.')
            return redirect('accounts:delete_account')

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            user_to_delete = User.objects.get(pk=request.user.pk)
            logout(request)
            user_to_delete.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('core:index')
        else:
            messages.error(request, 'Invalid password. Account not deleted.')

    return render(request, 'accounts/delete_account.html')