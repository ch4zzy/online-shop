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
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        String representation of the category object.
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a particular category instance.
        """
        return reverse('shop:product_list_by_category', 
                       args=[self.slug])


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
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'), )

    def __str__(self):
        """
        String representation of the product object.
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a particular product instance.
        """
        return reverse('shop:product_detail', args=[self.id, self.slug])


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
        __str__(): Returns a string representation of the comment, including the email of the user who wrote it.
    """
    post = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='comments',
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='user'
    )
    name = models.CharField(max_length=64)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        """
        String representation of the comment object.
        """
        return f'Comment by {self.email}'
