from django import forms


class CouponApplyForm(forms.Form):
    """
    A form for applying a coupon code to a shopping cart.

    Fields:
        code (CharField): the coupon code to apply.
    """

    code: forms.CharField = forms.CharField()
