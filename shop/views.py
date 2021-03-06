import os
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib import auth
from django.http import HttpResponse, Http404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import User
from django.contrib.auth.decorators import login_required
from decimal import *
from datetime import timedelta
from shop.form import *
from shop.models import *


def index(request):
    args = {}
    user = auth.get_user(request)

    products_Images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_Images.filter(product__category__id=1)
    products_images_notebooks = products_Images.filter(product__category__id=2)
    products_images_laptops = products_Images.filter(product__category__id=3)
    products_recent = products_Images.order_by('-id')[:4]

    print(products_Images)
    print(products_recent)

    if user.is_anonymous:
        args['products_Images'] = products_Images
        args['products_images_phones'] = products_images_phones
        args['products_images_notebooks'] = products_images_notebooks
        args['products_images_laptops'] = products_images_laptops
        args['products_recent'] = products_recent
        return render(request, 'shop/index/index.html', args)
    else:
        args['username'] = auth.get_user(request)
        args['products_Images'] = products_Images
        args['products_images_phones'] = products_images_phones
        args['products_images_notebooks'] = products_images_notebooks
        args['products_images_laptops'] = products_images_laptops
        args['products_recent'] = products_recent
        return render(request, 'shop/index/index.html', args)


def my_orders(request):
    args = {}
    user = auth.get_user(request)

    orders_my = Order.objects.filter(status__is_active=True, user__username=user, is_completed=False)
    products_in_order = ProductInOrder.objects.filter(order__user__username=user)

    orders_my_performed = Order.objects.filter(status__is_active=True, user__username=user, is_completed=True)

    print(orders_my)
    print(products_in_order)
    print(user)

    if user.is_anonymous:
        return render(request, 'shop/my_orders.html', args)
    else:
        args['username'] = auth.get_user(request)
        args['orders_my'] = orders_my
        args['products_in_order'] = products_in_order

        args['orders_my_performed'] = orders_my_performed
        return render(request, 'shop/my_orders.html', args)

def login(request):
    args = {}
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "???????????????????????? ???? ????????????!"
            return render(request, 'shop/login.html', args)
    else:
        return render(request, 'shop/login.html', args)


def register(request):
    args = {'form': UserSignUpForm}
    if request.POST:
        newuser_form = UserSignUpForm(request.POST)
        if request.POST['password'] != request.POST['password_confirmation']:
            return redirect('/register/')
        elif newuser_form.is_valid():
            newuser = User.objects.create(username=request.POST['username'],
                                          email=request.POST['email'],
                                          )
            newuser.set_password(request.POST['password_confirmation'])
            newuser.save()
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'shop/register.html', args)



def logout(request):
    auth.logout(request)
    return redirect('/')


def product(request, product_id):
    args = {}
    user = auth.get_user(request)

    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    if user.is_anonymous:
        args['product'] = product
        return render(request, 'shop/product.html', args)
    else:
        args['username'] = auth.get_user(request)
        args['product'] = product
        return render(request, 'shop/product.html', args)


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key.encode('utf-8')
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={"nmb": nmb})
        if not created:
            print("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = list()

    for item in  products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key.encode('utf-8')
    username = auth.get_user(request)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    print(products_in_basket)
    for item in products_in_basket:
        print(item.order)

    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name", "3423453")
            phone = data["phone"]

            comments = data["comments"]
            user = auth.get_user(request)
            name = user.username.encode('utf-8')
            address = data["address"].encode('utf-8')
            email = user.email
            print(user)

            order = Order.objects.create(user=user, 
                                        customer_name=name, 
                                        customer_email=email,
                                        customer_phone=phone,
                                        comments=comments, 
                                        customer_address=address, 
                                        status_id=1)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    print(type(value))

                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print("no")
    return render(request, 'shop/checkout.html', locals())



def confirm_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_completed = True
    order.save()
    return redirect('/my_orders')
