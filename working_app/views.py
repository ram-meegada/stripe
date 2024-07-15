# from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
# from django.shortcuts import get_object_or_404, redirect
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
# import stripe
# from main_project import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
import os
from django.http import HttpResponse
import random
from django.core.files.storage import FileSystemStorage
import pptxtopdf
from rest_framework.response import Response
import logging
from .models import AbilityModel

logger = logging.getLogger(__name__)
# stripe.api_key = settings.STRIPE_ACCOUNT_KEY

class LoginUser(TemplateView):
    template_name = "login.html"
    def post(self, request):
        user = get_object_or_404(User, username = request.POST["username"])
        return HttpResponseRedirect(reverse('homepage_api'))

class HomePageView(TemplateView):
    template_name = "homepage.html"
    def post(self, request):
        payment_link = payment_checkout_link()
        return redirect(payment_link.url)        
    
class SuccessView(TemplateView):
    template_name = "success.html"
    def get(self, request):
        return render(request, self.template_name)

class CancelView(TemplateView):
    template_name = "cancel.html"
    def get(self, request):
        return render(request, self.template_name)

# @method_decorator(csrf_exempt, name = 'dispatch')
class MyWebHookView(TemplateView):
    def get(self, request):
        print("webhook is hit")
        return HttpResponse("Success")
    
def payment_checkout_link():
    session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': "usd",
                        'product_data': {
                            'name': "Total Amount",
                        },
                        'unit_amount': 45 * 100,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= 'http://127.0.0.1:8000/success/',
            cancel_url= 'http://127.0.0.1:8000/cancel/',
        )
    return session    

from rest_framework.views import APIView
from django.views import View
from .models import TestModel

class TestView(APIView):
    # template_name = "test.html"
    def post(self, request):
        images = dict(request.data).get("myfile")
        # print(image.read(), '--------------')
        print(images, '----------')
        t = TestModel()
        for i in images:
            t.image = i
            t.save()
        

class Test(TemplateView):
    template_name = "test.html"
    def post(self, request):
        return HttpResponse("done")
    
class PptToPdfView(APIView):
    def get(self, request):
        import shutil
        from pptxtopdf import convert
        try:
            # file = request.FILES.get("file")
            # FILE_NAME = file.name
            # file_name = file.name.replace(" ", '').split(".")[0]
            # name = f"{random.randint(1000, 9999)}_{file_name}"
            # create_directory = os.mkdir(name)
            # fs = FileSystemStorage()
            # fs.save(f"{name}/{FILE_NAME}", file)
            # input_dir = f"D:/local/Practice/main_project/{name}"
            # output_dir = f"D:/local/Practice/main_project/{name}"
            logger.debug('This is a debug message')

            # Log some info
            logger.info('This is an info message')

            # Log a warning
            logger.warning('This is a warning message')

            # Log an error
            logger.error('This is an error message')

            # Log a critical message
            logger.critical('This is a critical message')
            # convert(input_dir, output_dir)
            # shutil.rmtree(input_dir)
            return Response({"data": "", "message": "Done", "status": 200})    
        except Exception as err: 
            return Response({"data": str(err), "message": "err", "status": 400})    
        
class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        pass

# class TestView(APIView):
def run_query():
    from django.db.models import When, Case, Value, F

    print("The query ran successfully ******************")

run_query()
