from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.coupons.forms import CouponApplyForm
from apps.shop.models import Product


@require_POST
def cart_add(request: HttpRequest, product_id: int) -> HttpResponseRedirect:
    """
    View function to add a product to the cart.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to add to the cart.

    Returns:
        HttpResponseRedirect: A redirect to the cart detail page.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], override_quantity=cd["update"])
    return redirect("cart:cart_detail")


def cart_remove(request: HttpRequest, product_id: int) -> HttpResponseRedirect:
    """
    View function to remove a product from the cart.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to remove from the cart.

    Returns:
        HttpResponseRedirect: A redirect to the cart detail page.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request: HttpRequest) -> HttpResponse:
    """
    View function to display the contents of the cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "update": True}
        )
    return render(
        request,
        "cart/detail.html",
        {
            "cart": cart,
            "coupon_apply_form": coupon_apply_form,
        },
    )
