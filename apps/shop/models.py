from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Model representing a product category.

    Attributes:
        name (str): The name of the category.
        slug (str): The unique slug for the category.

    Meta:
        ordering (tuple): The default sorting for the model.
        verbose_name (str): The human-readable name for a single object.
        verbose_name_plural (str): The human-readable name for multiple objects.
    """

    name: str = models.CharField(max_length=255, db_index=True)
    slug: str = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering: tuple = ("name",)
        verbose_name: str = "Category"
        verbose_name_plural: str = "Categories"

    def __str__(self) -> str:
        """
        String representation of the category object.
        """
        return self.name

    def get_absolute_url(self) -> str:
        """
        Returns the URL to access a particular category instance.
        """
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        category (Category): The category to which the product belongs.
        name (str): The name of the product.
        slug (str): The unique slug for the product.
        image (ImageField): The image associated with the product.
        description (str): The description of the product.
        price (Decimal): The price of the product.
        available (bool): Whether the product is available or not.
        created (DateTimeField): The date and time the product was created.
        updated (DateTimeField): The date and time the product was last updated.

    Meta:
        ordering (tuple): The default sorting for the model.
        index_together (tuple): A list of two-tuples specifying which fields to index together.

    Methods:
        get_absolute_url(): Returns the URL to access a detail record for this product.
    """

    category: Category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name: str = models.CharField(max_length=255, db_index=True)
    slug: str = models.SlugField(max_length=255, db_index=True)
    image: models.ImageField = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description: str = models.TextField(blank=True)
    price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)
    available: bool = models.BooleanField(default=True)
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: tuple = ("name",)
        index_together: tuple = (("id", "slug"),)

    def __str__(self) -> str:
        """
        String representation of the product object.
        """
        return self.name

    def get_absolute_url(self) -> str:
        """
        Returns the URL to access a particular product instance.
        """
        return reverse("shop:product_detail", args=[self.id, self.slug])


class Comment(models.Model):
    """
    Model representing a comment on a product.

    Attributes:
        post (Product): The product being commented on.
        user (User): The user who wrote the comment.
        name (str): The name of the user who wrote the comment.
        email (str): The email of the user who wrote the comment.
        body (str): The content of the comment.
        created (DateTimeField): The date and time the comment was created.
        active (bool): Whether the comment is currently active or not.

    Meta:
        ordering (tuple): The default sorting for the model.

    Methods:
        __str__(): Returns a string representation of the comment,
            including the email of the user who wrote it.
    """

    post: Product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user: User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    name: str = models.CharField(max_length=64)
    email: str = models.EmailField()
    body: str = models.TextField()
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    active: bool = models.BooleanField(default=False)

    class Meta:
        ordering: tuple = ("created",)

    def __str__(self) -> str:
        """
        String representation of the comment object.
        """
        return f"Comment by {self.email}"
