from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from apps.coupons.models import Coupon

# Local
from apps.shop.models import Product


class Order(models.Model):
    """
    A model for orders.

    Attributes:
        first_name (models.CharField): The first name of the customer.
        last_name (models.CharField): The last name of the customer.
        email (models.EmailField): The email address of the customer.
        address (models.CharField): The address of the customer.
        postal_code (models.CharField): The postal code of the customer.
        city (models.CharField): The city of the customer.
        created (models.DateTimeField): The date and time the order was created.
        updated (models.DateTimeField): The date and time the order was last updated.
        paid (models.BooleanField): Indicates whether the order has been paid for.
        braintree_id (models.CharField): The ID of the transaction in the Braintree payment system.
        coupon (models.ForeignKey): The coupon applied to the order.
        discount (models.IntegerField): The discount applied to the order.

    Methods:
        __str__(): The string representation of the Order model.
        get_absolute_url(): The URL for the Order model.
        get_total_cost(): The total cost of the Order model.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    coupon = models.ForeignKey(
        Coupon,
        related_name="orders",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        """
        Returns the string representation of the Order model.

        Returns:
            str: The string representation of the Order model.
        """
        return f"Order {self.id}"

    def get_absolute_url(self):
        """
        Returns the URL for the Order model.

        Returns:
            str: The URL for the Order model.
        """
        return reverse("orders:user_order_detail", args=[self.id])

    def get_total_cost(self):
        """
        Returns the total cost of the Order model.

        Returns:
            decimal.Decimal: The total cost of the Order model.
        """
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal("100"))


class OrderItem(models.Model):
    """
    A line item of a product included in an order.

    Attributes:
        order (Order): The order that this item belongs to.
        product (Product): The product that this item represents.
        price (Decimal): The price of the product at the time the order was placed.
        quantity (int): The quantity of the product ordered.

    Methods:
        __str__(): Returns a string representation of the item.
        get_cost(): Returns the total cost of the item.
    """

    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """
        Returns a string representation of the item, consisting of its ID.
        """
        return str(self.id)

    def get_cost(self):
        """
        Returns the total cost of the item, calculated as the price multiplied by the quantity.
        """
        return self.price * self.quantity
