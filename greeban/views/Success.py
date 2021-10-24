from django.views import View
from django.shortcuts import render, HttpResponse
import razorpay

from greeban.models import Order,Promotions,UserData
from django.core.mail import send_mail
from django.conf import settings


class Success(View):
    def get(self,request):
        request.session['cart'] = {}
        return render(request,'greeban/success.html')

    def post(self,request):
        client = razorpay.Client(auth=("rzp_test_JPNRqEHyI2pb9v", "VHPTND9VxAUKpRl62iVCuboN"))
        request.session['cart'] = {}
        response = request.POST
        promocode=request.POST.get("promocode")
        promoObj = Promotions.objects.filter(promocode=promocode)
        res = promoObj.values_list('times_used')[0]
        count = int(res[0])
        promoObj.update(times_used=count+1)
        emailId=str(promoObj.values_list('influencer_email')[0][0])
        print(emailId, "email id ")
        params_dict = {
            'razorpay_payment_id' : response['razorpay_payment_id'],
            'razorpay_order_id' : response['razorpay_order_id'],
            'razorpay_signature' : response['razorpay_signature']
        }
        # for sending email to influencer
        subject = "Regarding order at Greeeban"
        mailBody = "Using your promocode order has been placed at greeban"
        sendEmail(emailId, subject, mailBody)
        # for sending email to user
        session=request.session.get('userId')
        userObj = UserData.objects.all().get(
        user_id=session
        )
        emailId=userObj.email

        subject = "Regarding order at Greeeban"
        mailBody = "you successfully booked your order at greeban. Have a great day"
        sendEmail(emailId, subject, mailBody)

        # VERIFYING SIGNATURE
        try:
            status = client.utility.verify_payment_signature(params_dict)
            Order.objects.filter(transaction_id=response['razorpay_order_id']).update(transaction_status='Success')
            return render(request, 'greeban/success.html', {'status': 'Payment Successful'})
        except:
            Order.objects.filter(transaction_id=response['razorpay_order_id']).update(transaction_status='failed')
            return render(request, 'greeban/success.html', {'status': 'Payment Faliure!!!'})
        #return render(request,'greeban/test.html')

def sendEmail(to,subject,mailBody):
    emailId = str(to)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [emailId, ]
    send_mail(subject, mailBody, email_from, recipient_list)
