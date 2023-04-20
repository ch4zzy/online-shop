from django.contrib import admin

from apps.coupons.models import Coupon


class CouponAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the `Coupon` model.

    This class configures how the `Coupon` model is displayed and filtered in the Django
    admin panel. It also provides a search field to look up coupons by their code.

    Attributes:
        list_display (list): List of fields to display in the coupon list view.
        list_filter (list): List of fields to use for filtering coupons in the list view.
        search_fields (list): List of fields to use for searching coupons in the list view.

    """

    list_display: list[str] = ["code", "valid_from", "valid_to", "discount", "active"]
    list_filter: list[str] = ["active", "valid_from", "valid_to"]
    search_fields: list[str] = ["code"]


admin.site.register(Coupon, CouponAdmin)
