from django.views import View
from django.shortcuts import render, HttpResponse
import razorpay
from greeban.models import OrderDetails, Product, Order, UserData
import datetime


class Checkout(View):

    def get(self, request):
        """
        :param request: click on the checkout link
        :return: return the HTML page redirecting to checkout page
        """
        context = {}
        return render(request, 'greeban/checkout.html', context)

    '''
    def post(self, request):

        fullname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email_id')
        pin = request.POST.get('pin')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        order_amount = request.POST.get('total_amount')
        order_currency = 'INR'
        o_id = OrderDetails.objects.all().count()
        order_receipt = "Order_receiptID "+str(o_id)
        response = client.order.create(
            dict(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=address, payment_capture='0'))
        response_order_id = response['id']
        response_order_status = response['status']

        if response_order_status == 'created':
            context = {'price': order_amount, 'name': fullname, 'phone': mobile, 'email': email}
            # Server data for user convinience

            return render(request, "greeban/checkout.html", context=context)

        else:
            return HttpResponse("<h2> Error in processing your request</h2>")
    '''

    def post(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_ids(ids)
        print(products)
        price = int(request.POST.get('price'))
        promocode = request.POST.get('promocode')
        print(price,"pricee")
        print(promocode,"promocode")
        amount = price * 100
        cart = request.session['cart']

        orderId = len(Order.objects.all()) + 1
        user_id = request.session.get('userId')
        user = UserData.objects.get(user_id=user_id)
        finalOrder = Order(
            order_id=orderId,
            user_id=user,
            order_date=datetime.datetime.now(),
            transaction_status='Initiated',
            name=user.name,
            contactNo=str(user.mobile_no),
            emailId=user.email,
            address=user.address,
            city=user.city,
            state=user.state,
            pinCode=str(user.pin)
        )
        #finalOrder.save()
        orderDet = []
        total_amount = 0
        for product_id, product_quantity in cart.items():
            product = Product.objects.get(id=int(product_id))
            # print(product.product_price)
            order_detail_id = str(orderId)+product_id
            productData = OrderDetails(
                order_details_id=int(order_detail_id),
                product_id=product,
                quantity=product_quantity,
                price=product.product_price,
                total=product.product_price * product_quantity,
                order_id=finalOrder
            )
            orderDet.append(productData)
            total_amount = total_amount + product.product_price * product_quantity
        finalOrder.total_amount = price
        finalOrder.save()
        for order in orderDet:
            order.save()
        transaction_status = 'failed'
        client = razorpay.Client(auth=("rzp_test_JPNRqEHyI2pb9v", "VHPTND9VxAUKpRl62iVCuboN"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        if payment['status'] == 'created':
            transaction_status = 'created'
        else:
            transaction_status = 'failed'

        Order.objects.filter(order_id=orderId).update(transaction_status=transaction_status, transaction_id=payment['id'])
        context = {'payment_id': payment['id'], 'amount': price, 'cart': request.session.get('cart'),
                   'products': products,"promocode":promocode}
        return render(request, 'greeban/checkout.html', context)
