from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    active = models.BooleanField()

    class Meta:
        ordering = ('-valid_from', )

    def __str__(self):
        return self.code
