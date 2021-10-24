from django.views import View
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from greeban.models import Product,UserData
from django.http import JsonResponse
from django.core import serializers
import json
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import datetime
import random


class Home(View):
    def get(self, request):
        """
        :param request: click on the homepage link
        :return: html page redirecting to homepage
        """
        categories = Product.get_all_categories()
        print(categories)
        products = None
        cat = request.GET.get('category')
        if cat:
            products = Product.get_product_by_category(cat)
            print("categorywise product:", products)
        else:
            products = Product.get_product_by_category(categories[0])
            # print("category0wise product:", products)
        # print("URL testing", request.GET)
        no_of_categories = len(categories)
        context = {'products': products, 'categories': categories, 'range': no_of_categories}

        return render(request, 'greeban/home.html', context)

    def post(self, request):

        post_data = json.loads(request.body.decode("utf-8"))
        # prod = request.POST.get('prod')
        prod = str(post_data['prod'])
        cart = request.session.get('cart')
        try:
            remove = str(post_data['remove'])
        except:
            remove = False
        if cart:
            quantity = cart.get(prod)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(prod)
                    else:
                        cart[prod] = quantity - 1
                else:
                    cart[prod] = quantity + 1
            else:
                if not remove:
                    cart[prod] = 1
        else:
            if prod:
                cart = {prod: 1}

        request.session['cart'] = cart
        return JsonResponse({"msg": "Action Performed", "cart": cart})
        # return HttpResponseRedirect(request.path_info)


def get_products_by_category(request):
    cat = request.GET['category']
    categories = Product.get_all_categories()[1:]
    products = None
    if cat:
        products = Product.get_product_by_category(cat)
    else:
        products = Product.get_product_by_category(categories[0])
    no_of_categories = len(categories)
    return JsonResponse({"msg": "You Got the Response", "data": serializers.serialize('json', products)})


def get_quantity(request, pk):
    try:
        keys = request.session.get('cart').keys()
        for id in keys:
            if id != '':
                if id != "null" and int(id) == pk:
                    return JsonResponse({"Q": request.session.get('cart').get(id)})
        return JsonResponse({"Q": 0})
    except:
        return JsonResponse({"Q": 0})


@csrf_exempt
def sendEmail(request):
    post_data = json.loads(request.body.decode("utf-8"))
    emailId = str(post_data['EmailID'])
    subject = 'No-Reply OTP from Greenban Site'
    OTP = generateOTP()
    message = f'OTP is ${OTP}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [emailId, ]
    send_mail(subject, message, email_from, recipient_list)
    response = HttpResponse('OTP SENT')
    ## response.set_cookie(response, 'OTP', OTP)
    response.set_cookie('OTP', OTP, max_age=10 * 60)
    return response

@csrf_exempt
def activateSession(request):
    post_data = json.loads(request.body.decode("utf-8"))
    emailId = str(post_data['EmailID'])
    request.session['userId'] = emailId
    response = HttpResponse('success')
    print("session created")
    userDetails={'user_id':request.session['userId']}
    resp = UserData.objects.update_or_create(
        user_id=emailId,
        defaults=userDetails
    )
    return response


"""
def set_cookie(response, key, value, minute_expire=10):
    if days_expire is None:
        max_age = 10 * 60  # one year
    else:
        max_age = minute_expire * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )
"""


def generateOTP():
    number = random.randint(1000, 9999)
    return number
