from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

# Local
from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created
from apps.cart.cart import Cart

# Create your views here.


def order_create(request):
    cart = Cart(request)
    user = request.user
    initial_data = {
                'first_name': user.first_name, 
                'email': user.email,
        }
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                if cart.coupon:
                    order.coupon = cart.coupon
                    order.discount = cart.coupon.discount
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                cart.clear()
                order_created.delay(order.id)
                request.session['order_id'] = order.id
                return redirect(reverse('payment:process'))
        else:
            form = OrderCreateForm(initial=initial_data)
    else: 
        return redirect('login')
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

@login_required
def user_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="order_{order.id}.pdf"'
    weasyprint.HTML(string=html).write_pdf(response, 
                                           stylesheets=[weasyprint.CSS(
                                                settings.STATIC_PDF + '/css/pdf.css')])
    return response
