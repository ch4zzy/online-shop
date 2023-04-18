from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.coupons.forms import CouponApplyForm
# Local
from apps.shop.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, product_id):
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
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
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
    return redirect('cart:cart_detail')


def cart_detail(request):
    """
    View function to display the contents of the cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True
                     }
        )
        coupon_apply_form = CouponApplyForm()
    return render(
        request, 'cart/detail.html', 
        {
            'cart': cart,
            'coupon_apply_form': coupon_apply_form,
        }
    )
