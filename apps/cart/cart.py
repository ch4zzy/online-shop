from decimal import Decimal

from django.conf import settings

from apps.coupons.models import Coupon

# Local
from apps.shop.models import Product


class Cart(object):
    """
    Class representing a shopping cart for a user.

    Attributes:
    - session: session data for the cart
    - cart: dictionary of cart items
    - coupon_id: id of the coupon applied to the cart

    Methods:
    - __init__(self, request): Constructor that initializes the cart object
    - __iter__(self): Allows the cart object to be iterated over
    - __len__(self): Returns the total number of items in the cart
    - add(self, product, quantity=1, override_quantity=False): Adds a product to the cart
    - save(self): Saves the cart to the session
    - remove(self, product): Removes a product from the cart
    - clear(self): Clears the cart by removing it from the session
    - get_total_price(self): Returns the total price of all items in the cart
    - coupon(self): Getter method for the coupon applied to the cart
    - get_discount(self): Returns the discount applied to the cart based on the coupon
    - get_total_price_after_discount(self): Returns the total price of all items in the cart after applying the coupon discount
    """

    def __init__(self, request):
        """
        Constructor that initializes the cart object.

        Parameters:
        - request: the request object
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get("coupon_id")

    def __iter__(self):
        """
        Allows the cart object to be iterated over.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Returns the total number of items in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """
        Adds a product to the cart.

        Parameters:
        - product: the product to add
        - quantity: the quantity of the product to add (default=1)
        - override_quantity: whether to override the quantity of an existing product in the cart (default=False)
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        """
        Saves the cart to the session.
        """
        self.session.modified = True

    def remove(self, product):
        """
        Removes a product from the cart.

        Parameters:
        - product: the product to remove
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """
        Remove all items from the cart session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.

        Returns:
            Decimal: The total price.
        """
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    @property
    def coupon(self):
        """
        Get the coupon object associated with the cart.

        Returns:
            Coupon or None: The Coupon object or None if no coupon is associated with the cart.
        """
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        """
        Calculate the discount amount based on the coupon associated with the cart.

        Returns:
            Decimal: The discount amount.
        """
        if self.coupon:
            return self.coupon.discount / Decimal("100") * self.get_total_price()
        return Decimal("0")

    def get_total_price_after_discount(self):
        """
        Calculate the total price after applying the coupon discount.

        Returns:
            Decimal: The total price after the discount.
        """
        return self.get_total_price() - self.get_discount()
