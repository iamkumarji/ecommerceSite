from django.views import View
from django.shortcuts import render, HttpResponseRedirect
from greeban.models import Product, Promotions
from django.http import JsonResponse
import json
from django.shortcuts import render, HttpResponseRedirect, HttpResponse

class Cart(View):
    def get(self, request):
        """
        :param request: click on the cart link
        :return: returns the HTML page redirecting to cart page
        """
        cart = request.session.get('cart')
        if cart:
            if 'null' in cart.keys():
                cart.pop('null')
            ids = list(request.session.get('cart').keys())
            ids = [id for id in ids if id != '']
            if len(ids) > 0:
                print('cart items exists')
                products = Product.get_products_by_ids(ids)
                return render(request, 'greeban/cart.html', {"products": products})
            else:
                print("No cart item")
                context = {"range": 0}
                return render(request, 'greeban/cart.html', context)

        else:
            request.session['cart'] = {}
            print("No cart item")
            context = {"range": 0, "cart": request.session.get('cart')}
            return render(request, 'greeban/cart.html', context)

    def post(self, request):
        # name = request.POST.get('fullname')
        # mobile = request.POST.get('phonenumber')
        # email = request.POST.get('emailid')
        # pin = request.POST.get('pincode')
        # state = request.POST.get('state')
        # city = request.POST.get('city')
        # address = request.POST.get('address')
        # print(name, mobile, email, pin, state, city, address)
        # price = int(request.POST.get('price'))
        # print(price)
        # amount = price * 100
        # client = razorpay.Client(auth=("rzp_test_JPNRqEHyI2pb9v", "VHPTND9VxAUKpRl62iVCuboN"))
        # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        # context = {'payment_id': payment['id'], 'amount': amount}
        # return JsonResponse(context,safe=False)
        # return render(request, 'greeban/checkout.html', context)
        return render(request, 'greeban/cart.html')

def applyPromotions(request):
    post_data = json.loads(request.body.decode("utf-8"))
    code = str(post_data['code'])
    try:
        codeObj = Promotions.objects.get(promocode=code)
        codeObj.times_used=codeObj.times_used+1;
        codeObj.save()
        response = HttpResponse(codeObj.discount_percent)
    except:
        response = HttpResponse('failure')
    return response
