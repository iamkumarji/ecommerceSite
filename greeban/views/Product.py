from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from greeban.models import Product
from math import ceil


class ProductView(View):
    def get(self, request, myid):
        """
            :param myid: product id
            :param request: click on the product(page) link
            :return: return HTML page redirecting to product page
            """
        # request.session.clear()
        cart = request.session.get('cart')
        sum = 0
        for i in cart.values():
            sum += i
        print(sum)
        if not cart:
            request.session.cart = {}
        # fetching individual product
        mainproduct = Product.objects.filter(id=myid)
        res = mainproduct.values_list('product_category')[0]
        cat = res[0]
        print(cat)
        # print(Product.objects.filter(id=1))
        # fetching all products for slider
        #products = Product.objects.all()
        pro = Product.objects.exclude(id=myid)
        print(len(pro))
        products = pro.filter(product_category=cat)
        allcat_prod = Product.objects.all()
        print(len(allcat_prod))
        n = len(products)
        print(n)
        nSildes = n // 4 + ceil((n / 4) - (n // 4))
        print(nSildes)
        params = {'no_of_slides': nSildes, 'range': range(1, nSildes), 'product': products,
                  'mainproduct': mainproduct[0],'cart_items':sum,'prod_cat':allcat_prod}
        # print(products)
        return render(request, 'greeban/product.html', params)

    def post(self, request, myid):
        return render(request, 'greeban/product.html')
        '''
        prod = request.POST.get('prod')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        print("cart")

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
        
        # print(request.session['cart'])
        return HttpResponseRedirect(request.path_info)
        # return HttpResponse('ok')

        '''
