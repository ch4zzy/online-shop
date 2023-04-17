from django.contrib import admin
from django.http import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
import csv
import datetime

# Local
from apps.orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Tabular inline view for OrderItem model in OrderAdmin
    """
    model = OrderItem
    raw_id_fields = ['product']


def export_to_csv(modeladmin, request, queryset):
    """
    Action that exports selected Orders to a CSV file.

    Args:
        modeladmin (admin.ModelAdmin): The ModelAdmin instance.
        request (HttpRequest): The HttpRequest instance.
        queryset (QuerySet): The queryset of Order instances to export.

    Returns:
        HttpResponse: The HTTP response with the CSV file.
    """
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;'\
        f'filename={opts.verbose_name}.csv'
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() \
              if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


def order_detail(obj):
    """
    Returns a link to the detail page for an Order.

    Args:
        obj (Order): The Order instance.

    Returns:
        str: A link to the detail page for the Order.
    """
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f"<a href='{url}'>View</a>")


def order_pdf(obj):
    """
    Returns a link to generate a PDF for an Order.

    Args:
        obj (Order): The Order instance.

    Returns:
        str: A link to generate a PDF for the Order.
    """
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f"<a href='{url}'>PDF</a>")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    ModelAdmin class for the Order model.

    Defines the behavior of the admin interface for Order instances.
    """
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail, order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]
