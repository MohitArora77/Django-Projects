from django.urls import path
from shopping_app import views

urlpatterns = [
    path('login/',views.login_view),
    path('cart/',views.cart_view),
    path('Order/',views.order_view),
    ]