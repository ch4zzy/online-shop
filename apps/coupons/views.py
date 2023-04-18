from apps.coupons.forms import CouponApplyForm
# Local
from apps.coupons.models import Coupon
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST


@require_POST
def coupon_apply(request):
    """
    Apply a coupon to the current cart session if it is valid and active.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the cart detail page after applying the coupon.
    """
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
