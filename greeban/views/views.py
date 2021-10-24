from django.shortcuts import render
from django.http import HttpResponse
from greeban.models import Product
from math import ceil
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# def home(request):


def product(request, myid):
    """
    :param myid: product id
    :param request: click on the product(page) link
    :return: return HTML page redirecting to product page
    """
    # fetching individual product
    mainproduct = Product.objects.filter(id=myid)

    # fetching all products for slider
    products = Product.objects.all()
    n = len(products)
    nSildes = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSildes, 'range': range(1, nSildes), 'product': products, 'mainproduct': mainproduct[0]}
    # print(products)
    return render(request, 'greeban/product.html', params)


# def checkout(request):



# def recipe(request):


