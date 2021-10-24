from django.views import View
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from greeban.models import Product
from django.http import JsonResponse
from greeban.models import UserData
import razorpay

from django.http import JsonResponse
import json
class Profile(View):
    def get(self, request):
        return render(request, 'greeban/profile.html')

    def post(self, request):
        return render(request, 'greeban/profile.html')

    def addUserInfo(request):
        session = request.session.get('userId')
        post_data = json.loads(request.body.decode("utf-8"))
        userDetails = dict(post_data['userDetails'])
        print(userDetails, "userDetails")
        print(userDetails.get("phonenumber"))

        resp = UserData(
            mobile_no=int(userDetails.get("phonenumber")),
            name=userDetails.get("fullname"),
            email=userDetails.get("emailid"),
            pin=int(userDetails.get("pincode")),
            state=userDetails.get("state"),
            city=userDetails.get("city"),
            address=userDetails.get("address")
        ).save()

        print(resp, "database")
        # print("156"+request.session['userId'])
        response = HttpResponse('success')

        ## response.set_cookie(response, 'OTP', OTP
        return response

def checkUserExist(request):
    # check if user is email or phone number
    # To be checked if phone number and email
    # if email
    session = request.session.get('userId')
    # if phone
    # session= phone code

    post_data = json.loads(request.body.decode("utf-8"))
    print(session,"session")
    try:
        # if else email or phone number
        resp=UserData.objects.get(email=session)
    except UserData.DoesNotExist:
        resp = False
    if(resp):
        print("Exist")
    else:
        print("NoExist")

    # resp2=UserData.objects.get(name="Vishal")
    print(resp,"resp2")

    # print("156"+request.session['userId'])
    response = HttpResponse(resp)
    ## response.set_cookie(response, 'OTP', OTP
    return response