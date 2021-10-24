from django.views import View
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from greeban.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from greeban.models import UserData
from greeban.views.Profile import checkUserExist
class Login(View):

    def get(self, request):
        """
        :param request: click on the cart link
        :return: returns the HTML page redirecting to cart page
        """
        """cart = request.session.get('cart')
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
            context = {"range": 0, "cart": request.session.get('cart')}"""
        #print("success")

        print(self.generate_token())
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




def checkLogin(request):
    try:
        session = request.session.get('userId')

        #print("156"+request.session['userId'])
        if session!=None:
            response = HttpResponse('success')
        else:
            response = HttpResponse('failure')

        print(session)
        ## response.set_cookie(response, 'OTP', OTP)
    except:
        response = HttpResponse('failure')
    return response

@csrf_exempt
def logout(request):
    try:
        del request.session['cart']
    except:
        pass
    try:
        del request.session['userId']
    except:
        pass
        #print("156"+request.session['userId'])
    response = HttpResponse('success')

        ## response.set_cookie(response, 'OTP', OTP)
    """except:
        response = HttpResponse('failure')"""
    return response

def addUserInfo(request):
        session = request.session.get('userId')
        post_data = json.loads(request.body.decode("utf-8"))
        userDetails = dict(post_data['userDetails'])
        print(userDetails,"userDetails")
        print(userDetails.get("phonenumber"))

#        if(checkUserExist(request)=='')
        """
        resp=UserData.objects.update_or_create(
        mobile_no= int(userDetails.get("phonenumber")),
        name = userDetails.get("fullname"),
        email = userDetails.get("emailid"),
        pin = int(userDetails.get("pincode")) ,
        state = userDetails.get("state"),
        city = userDetails.get("city"),
        address = userDetails.get("address")
        ).save()"""

        resp = UserData.objects.update_or_create(
        user_id=session,
        defaults=userDetails
        )

        #checkUserExist(request)
        
        print(resp,"database")

        response = HttpResponse('success')

        return response


def getUserInfo(request):

    session = request.session.get('userId')

    res = UserData.objects.all().get(
        user_id=session
    )
    response={}
    print(res, "database")
#    print(response['name'], "database")
    print(res.name)
    response['name']=res.name
    response['mobile_no']=res.mobile_no
    response['email']=res.email
    response['pin']=res.pin
    response['state']=res.state
    response['city']=res.city
    response['address']=res.address

    return JsonResponse(response)