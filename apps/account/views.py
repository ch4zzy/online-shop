from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.account.forms import (
    LoginForm,
    ProfileEditForm,
    UserEditForm,
    UserRegistration,
)
from apps.account.models import Profile
from apps.orders.models import Order


def user_login(request: HttpRequest) -> HttpResponse:
    """
    Authenticates a user for login using their username and password.

    Parameters:
    request (HttpRequest): The request object for the current request.

    Returns:
    HttpResponse: If the user is successfully authenticated and is active, returns a success message;
                  If the user is inactive, returns an "Account disabled" message;
                  If the user cannot be authenticated, returns an "Invalid login" message;
                  If the request method is not POST, returns the login page.

    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Successfully login")
            else:
                return HttpResponse("Account disabled")
        else:
            return HttpResponse("Invalid login")
    else:
        form = LoginForm
    return render(
        request,
        "account/login.html",
        {
            "form": form,
        },
    )


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    """
    Displays the dashboard page for a logged-in user, showing their orders.

    Parameters:
    request (HttpRequest): The request object for the current request.

    Returns:
    HttpResponse: Renders the dashboard page, passing a list of the user's orders,
                  the user's profile, and lists of the user's paid and unpaid orders.
    """
    if request.method == "GET":
        user = request.user
        orders = Order.objects.filter(email=user.email)
        orders_paid = orders.filter(paid=True)
        orders_unpaid = orders.filter(paid=False)
        return render(
            request,
            "account/dashboard.html",
            {
                "orders": orders,
                "user": user,
                "orders_paid": orders_paid,
                "orders_unpaid": orders_unpaid,
            },
        )


def register(request: HttpRequest) -> HttpResponse:
    """
    Handles registration of a new user.

    Parameters:
    request (HttpRequest): The request object for the current request.

    Returns:
    HttpResponse: If the request method is POST and the user registration form is valid,
                  creates a new user and redirects to the registration success page;
                  Otherwise, renders the registration page with the user registration form.
    """
    if request.method == "POST":
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(
                request,
                "account/register_done.html",
                {
                    "new_user": new_user,
                },
            )
    else:
        user_form = UserRegistration()
    return render(
        request,
        "account/register.html",
        {
            "user_form": user_form,
        },
    )


@login_required
def edit(request: HttpRequest) -> HttpResponse:
    """
    Handles editing of a user's profile.

    Parameters:
    request (HttpRequest): The request object for the current request.

    Returns:
    HttpResponse: If the request method is POST and the user and profile forms are valid,
                  saves the updated user and profile and displays a success message;
                  Otherwise, displays an error message and renders the edit page with the forms.
    """
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating profile.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account/edit.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )
