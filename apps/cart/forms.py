from django import forms

PRODUCT_QUANTITY_CHOICES: list[tuple[int, str]] = [(i, str(i)) for i in range(1, 12)]


class CartAddProductForm(forms.Form):
    """
    A form used to add a product to the cart.

    Attributes:
    ----------
    quantity : TypedChoiceField
        A field for selecting the quantity of the product to add.
    update : BooleanField
        A field indicating whether to update the quantity of the product
        if it is already in the cart.
    """

    quantity: forms.TypedChoiceField = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update: forms.BooleanField = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
