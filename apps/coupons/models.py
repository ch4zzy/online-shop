from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Coupon(models.Model):
    """
    Model representing a coupon which can be applied to an order to give a discount.
    """

    code: models.CharField = models.CharField(max_length=20, unique=True)
    valid_from: models.DateTimeField = models.DateTimeField()
    valid_to: models.DateTimeField = models.DateTimeField()
    discount: models.IntegerField = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    active: models.BooleanField = models.BooleanField()

    class Meta:
        ordering: tuple = ("-valid_from",)

    def __str__(self) -> str:
        return self.code
