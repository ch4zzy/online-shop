from django.shortcuts import render, get_object_or_404, redirect

# Local
from apps.shop.forms import CommentForm
from apps.shop.models import Category, Product
from apps.cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    """
    View that displays the list of available products or products belonging to a specific category.

    Parameters:
    request (HttpRequest): The HTTP request object.
    category_slug (str, optional): The slug of the category to filter by. Defaults to None.

    Returns:
    HttpResponse: The HTTP response object that contains the rendered template.

    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request, 'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        }
    )


def product_detail(request, id, slug):
    """
    View that displays the details of a specific product, including its comments and allows authenticated users to add a comment.

    Parameters:
    request (HttpRequest): The HTTP request object.
    id (int): The id of the product to display.
    slug (str): The slug of the product to display.

    Returns:
    HttpResponse: The HTTP response object that contains the rendered template.

    """
    template_name = 'product_detail.html'
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    post = product
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid:
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.user_id = request.user.id
                new_comment.save()
        else:
            comment_form = CommentForm()
    else: 
        return redirect('login')
    return render(
        request, 'shop/product/detail.html',
        {
            'product': product,
            'cart_product_form': cart_product_form,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        }
    )


def product_search(request):
    """
    View that searches for products based on a query string and displays the results.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response object that contains the rendered template.

    """
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products_search = Product.objects.filter(name__icontains=query)
            return render(
                request, 'shop/product/list.html',
                {
                    'products_search': products_search,
                    'query': query,
                }
            )
        else:
            return render(
                request, 'shop/product/list.html',
                {}
            )
