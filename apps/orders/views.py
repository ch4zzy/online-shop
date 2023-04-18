import weasyprint
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm

# Local
from apps.orders.models import Order, OrderItem
from apps.orders.tasks import order_created


def order_create(request):
    """
    View function that handles the creation of orders.

    If the user is authenticated, the view displays a form for creating a new order, pre-populated with
    the user's name and email. The view handles POST requests submitted by the form, validates the form data,
    and creates a new order and corresponding OrderItems if the form is valid.

    If the user is not authenticated, the view redirects them to the login page.

    After successfully creating a new order, the view schedules an asynchronous task to send a confirmation email
    to the user and redirects the user to the payment page.

    Returns:
        A rendered template displaying the order form and the contents of the user's cart.

        If the request method is not POST and the user is not authenticated, a redirect to the login page.
    """
    cart = Cart(request)
    user = request.user
    initial_data = {
        "first_name": user.first_name,
        "email": user.email,
    }
    if request.user.is_authenticated:
        if request.method == "POST":
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                if cart.coupon:
                    order.coupon = cart.coupon
                    order.discount = cart.coupon.discount
                order.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item["product"],
                        price=item["price"],
                        quantity=item["quantity"],
                    )
                cart.clear()
                order_created.delay(order.id)
                request.session["order_id"] = order.id
                return redirect(reverse("payment:process"))
        else:
            form = OrderCreateForm(initial=initial_data)
    else:
        return redirect("login")
    return render(
        request,
        "orders/order/create.html",
        {
            "cart": cart,
            "form": form,
        },
    )


@login_required
def user_order_detail(request, order_id):
    """
    View function that displays the details of a user's order.

    If the user is not authenticated, the view redirects them to the login page.

    Returns:
        A rendered template displaying the details of the specified order.

        If the user is not authenticated, a redirect to the login page.
    """
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        "orders/order/detail.html",
        {
            "order": order,
        },
    )


@staff_member_required
def admin_order_detail(request, order_id):
    """
    View function that displays the details of an order for an admin user.

    If the user is not authenticated as an admin user, the view redirects them to the login page.

    Returns:
        A rendered template displaying the details of the specified order.

        If the user is not authenticated as an admin user, a redirect to the login page.
    """
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        "admin/orders/order/detail.html",
        {
            "order": order,
        },
    )


@staff_member_required
def admin_order_pdf(request, order_id):
    """
    Generate a PDF version of an order for staff members.

    Args:
        request (HttpRequest): The HTTP request object.
        order_id (int): The ID of the order to generate a PDF for.

    Returns:
        HttpResponse: A PDF file containing the order information.
    """
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("orders/order/pdf.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'filename="order_{order.id}.pdf"'
    weasyprint.HTML(string=html).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_PDF + "/css/pdf.css")]
    )
    return response
