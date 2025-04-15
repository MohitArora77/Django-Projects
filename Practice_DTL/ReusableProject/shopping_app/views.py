from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return HttpResponse("<h1>Login to your Account</h1>")

def cart_view(request):
    return HttpResponse("<h1>Add to Cart</h1")

def order_view(request):
    return HttpResponse("<h1>Your Order</h1>")