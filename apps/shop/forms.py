# Local
from apps.shop.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    A form used for adding comments to a product.

    Attributes:
        Meta (class): The metadata class of the form.
            model (class): The model that the form is associated with.
            fields (tuple): A tuple of fields that the form contains.
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
