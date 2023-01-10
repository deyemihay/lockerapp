from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserLocker
from .forms import LockerForm, RegistrationForm


# Create your views here.
def home(request):
    return render(request, 'safelocker/home.html')


def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has registered successfully, please login.')
            return redirect('login-page')
    context = {'form': form}
    return render(request, 'safelocker/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist.')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You have logged in successfully as '{user.username}'")
            return redirect('home-page')
        else:
            messages.error(request, 'username or password does not exist.')

    context = {}
    return render(request, 'safelocker/login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home-page')


@login_required()
def user_locker(request):
    locker_items = UserLocker.objects.filter(user=request.user)
    context = {'locker_items': locker_items}
    return render(request, 'safelocker/user-locker.html', context)


def locker_form(request):
    form = LockerForm()
    if request.method == 'POST':
        form = LockerForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            messages.success(request, 'You have added to your locker successfully.')
            return redirect('user-locker')
    context = {'form': form}
    return render(request, 'safelocker/locker-form.html', context)


def selected_item(request, pk):
    item_select = None
    locker_items = UserLocker.objects.all()
    for i in locker_items:
        if i.id == int(pk):
            item_select = i
    context = {'item_select': item_select}
    return render(request, 'safelocker/locker-item.html', context)


def edit_item(request, pk):
    item = UserLocker.objects.get(id=pk)
    form = LockerForm(instance=item)

    if request.method == 'POST':
        form = LockerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your locker has been updated successfully.')
            return redirect('user-locker')

    context = {'form': form}
    return render(request, 'safelocker/locker-form.html', context)


def delete_item(request, pk):
    item = UserLocker.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('user-locker')
    return render(request, 'safelocker/delete.html', {'obj': item})


def user_profile(request):
    return render(request, 'safelocker/user-profile.html')


def delete_profile(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home-page')
    return render(request, 'safelocker/delete-user.html', {'object': user})
