from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name = "login_api"),
    path('homepage/', HomePageView.as_view(), name = "homepage_api"),
    path('success/', SuccessView.as_view(), name = "success_api"),
    path('cancel/', CancelView.as_view(), name = "cancel_api"),
    path('my-webhook/', MyWebHookView.as_view(), name = "webhook_api"),
] 