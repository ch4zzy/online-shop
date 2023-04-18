from apps.cart.cart import Cart


def cart(request):
    """
    Context processor function that adds a Cart object to the context of every request.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        dict: A dictionary with a single key "cart", which maps to a Cart object.
    """
    return {"cart": Cart(request)}
