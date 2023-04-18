from io import BytesIO

import braintree
import weasyprint
# Local
from apps.orders.models import Order
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string


def payment_process(request):
    """
    Handle payment processing for orders.

    If the request method is POST, get the payment method nonce and use it to charge the order amount with Braintree.
    If the transaction is successful, mark the order as paid and send an email with the order invoice attached as a PDF.
    Redirect to the payment done page.
    If the transaction fails, redirect to the payment canceled page.

    If the request method is GET, generate a client token for the Braintree drop-in UI and render the payment processing page.

    Parameters:
    - request: HTTP request object containing session data and form data

    Returns:
    - If the request method is POST and the transaction is successful, redirect to the payment done page.
    - If the request method is POST and the transaction fails, redirect to the payment canceled page.
    - If the request method is GET, render the payment processing page with a client token for Braintree.
    """
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })

        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            subject = f'Shop - Invoice no. {order.id}'
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject,
                                 message,
                                 'smtp.payment@gmail.com',
                                 [order.email])
            html = render_to_string('orders/order/pdf.html', {'order': order})
            out = BytesIO()
            stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
            email.attach(f'order_{order.id}.pdf',
                         out.getvalue(),
                         'application/pdf')
            email.send()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(
            request, 'payment/process.html',
            {
                'order': order,
                'client_token': client_token
                }
        )


def payment_done(request):
    """
    Render the payment done page.

    Parameters:
    - request: HTTP request object

    Returns:
    - Rendered payment done page template
    """
    return render(request, 'payment/done.html')


def payment_canceled(request):
    """
    Render the payment canceled page.

    Parameters:
    - request: HTTP request object

    Returns:
    - Rendered payment canceled page template
    """
    return render(request, 'payment/canceled.html')
