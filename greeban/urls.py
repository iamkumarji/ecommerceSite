from django.urls import path
from . import views
from .views.Cart import Cart, applyPromotions
from .views.Product import ProductView
from .views.Home import Home, get_products_by_category, get_quantity, sendEmail, activateSession
from .views.Checkout import Checkout
from .views.Receipe import Receipe
from .views.Success import Success
from .views.Login import checkLogin, logout, addUserInfo, getUserInfo
from .views.Profile import Profile
from .views.About import About
from .views.ReturnPolicy import ReturnPolicy
from .views.Termsandcondi import Termsandcondi
from .views.Privacypolicy import Privacypolicy

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('get_products/', get_products_by_category, name="Get_products"),
    path('get_quantity/<int:pk>/', get_quantity, name="Get_Q"),
    path('sendEmail', sendEmail, name='sendEmail'),

    path('product/<int:myid>', ProductView.as_view(), name="product"),
    path('cart/', Cart.as_view(), name="cart"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('success/', Success.as_view(), name="success"),
    path('recipe/', Receipe.as_view(), name="recipe"),
    path('checkLoginStatus', checkLogin, name="checkLoginStatus"),
    path('logout', logout, name="logout"),
    path('activateSession', activateSession, name="activateSession"),
    path('addUserInfo', addUserInfo, name="addUserInfo"),
    path('getUserInfo', getUserInfo, name="getUserInfo"),
    path('profile', Profile.as_view(), name="profile"),
    path('applyPromotions', applyPromotions, name="profile"),
    path('about/', About.as_view(), name="about"),
    path('returnpolicy/', ReturnPolicy.as_view(), name="returnpolicy"),
    path('termsandcondi/', Termsandcondi.as_view(), name="termsandcondi"),
    path('privacypolicy/', Privacypolicy.as_view(), name="privacypolicy"),
]
