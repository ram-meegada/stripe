from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import stripe
from main_project import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

stripe.api_key = settings.STRIPE_ACCOUNT_KEY

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

@method_decorator(csrf_exempt, name = 'dispatch')
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