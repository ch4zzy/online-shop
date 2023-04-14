from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Local
from .forms import LoginForm, UserRegistration, UserEditForm, ProfileEditForm
from .models import Profile
from apps.orders.models import Order


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Successfully login')
            else:
                return HttpResponse('Account disabled')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm
    return render(request, 
                  'account/login.html', 
                  {'form': form})


@login_required
def dashboard(request):
    if request.method == 'GET':
        user = request.user
        orders = Order.objects.filter(email=user.email)
        orders_paid = orders.filter(paid=True)
        orders_unpaid = orders.filter(paid=False)
        return render(request, 
                      'account/dashboard.html', 
                      {'orders': orders,
                       'user': user,
                       'orders_paid': orders_paid,
                       'orders_unpaid': orders_unpaid})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistration()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating profile.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})
