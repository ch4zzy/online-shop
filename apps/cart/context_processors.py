from typing import Any

from django.http import HttpRequest

from apps.cart.cart import Cart


def cart(request: HttpRequest) -> dict[str, Any]:
    """
    Context processor function that adds a Cart object to the context of every request.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        dict: A dictionary with a single key "cart", which maps to a Cart object.
    """
    return {"cart": Cart(request)}
