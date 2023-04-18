# Local
from apps.shop.models import Category, Comment, Product
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Customizes the appearance and behavior of the Category model in the admin interface.

    Attributes:
        list_display (tuple): A list of field names to display on the 
            change list page for Category model.
        prepopulated_fields (dict): A dictionary where the keys are field names and 
            the values are lists or tuples of field names.

    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Customizes the appearance and behavior of the Product model in the admin interface.

    Attributes:
        list_display (tuple): A list of field names to display on the 
            change list page for Product model.
        list_filter (tuple): A list of fields to filter the change 
            list by on the change list page.
        list_editable (tuple): A list of field names that can be 
            edited on the change list page.
        prepopulated_fields (dict): A dictionary where the keys are 
            field names and the values are lists or tuples of field names.

    """
    list_display = [
        'name', 'slug', 'price', 
        'available', 'created', 'updated'
        ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Customizes the appearance and behavior of the Comment model in the admin interface.

    Attributes:
        list_display (tuple): A list of field names to display on the 
            change list page for Comment model.
        list_filter (tuple): A list of fields to filter the change 
            list by on the change list page.
        search_fields (tuple): A list of fields to search in when the 
            user submits a search query.
        actions (tuple): A list of custom actions to display at the top 
            of the change list page.

    """
    list_display = ('name', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Approves selected comments in the admin interface.

        Args:
            request (HttpRequest): The current HttpRequest.
            queryset (QuerySet): A queryset containing the comments to approve.

        Returns:
            None

        """
        queryset.update(active=True)
