from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import loader, Context
from .models import Bride, Cart
from .forms import BrideCreate
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_POST
from bride.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CartCreate
from django.views.decorators.csrf import csrf_exempt


def aboutus(request):
    template = loader.get_template("aboutus.html")
    return HttpResponse(template.render())


def privacy(request):
    template = loader.get_template("privacy.html")
    return HttpResponse(template.render())


def information(request):
    template = loader.get_template("information.html")
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())


def stores(request):
    template = loader.get_template("stores.html")
    return HttpResponse(template.render())


def allproducts(request):
    shelf = Bride.objects.all()
    return render(request, 'allproducts.html', {'shelf': shelf})


def upload(request):
    upload = BrideCreate()
    if request.method == 'POST':
        upload = BrideCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('allproducts')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'upload'}}">reload</a>""")
    else:
        return render(request, 'bride/upload_form.html', {'upload_form': upload})


def update_bride(request, bride_id):
    bride_id = int(bride_id)
    try:
        bride_sel = Bride.objects.get(id=bride_id)
    except Bride.DoesNotExist:
        return redirect('allproducts')
    bride_form = BrideCreate(request.POST or None, instance=bride_sel)
    if bride_form.is_valid():
        bride_form.save()
        return redirect('allproducts')
    return render(request, 'bride/upload_form.html', {'upload_form': bride_form})


def delete_bride(request, bride_id):
    bride_id = int(bride_id)
    try:
        bride_sel = Bride.objects.get(id=bride_id)
    except Bride.DoesNotExist:
        return redirect('allproducts')
    bride_sel.delete()
    return redirect('allproducts')


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Success! Thank you for your message.')
    return render(request, "email.html", {'form': form})


def products(request):
    if request.method == 'GET':
        ward = Bride.objects.all()
    return render(request, 'products.html', {'ward': ward})


def products_sabyasachi(request):
    if request.method == 'GET':
        ward = Bride.objects.filter(brand="sabyasachi")
    return render(request, 'brands.html', {'ward': ward})


def products_manish(request):
    if request.method == 'GET':
        ward = Bride.objects.filter(brand="manish malhotra")
    return render(request, 'brands.html', {'ward': ward})


def products_ritu(request):
    if request.method == 'GET':
        ward = Bride.objects.filter(brand="ritu kumar")
    return render(request, 'brands.html', {'ward': ward})


def products_saree(request):
    if request.method == 'GET':
        ward = Bride.objects.filter(describe="saree")
    return render(request, 'brands.html', {'ward': ward})


def products_men(request):
    if request.method == 'GET':
        ward = Bride.objects.filter(describe="men")
    return render(request, 'brands.html', {'ward': ward})


def products_accessories(request):
    if request.method == 'GET':
        ward = Bride.objects.filter(describe="accessories")
    return render(request, 'brands.html', {'ward': ward})


def products_price(request):
    lowerVal = request.GET.get('lowerVal', '')
    upperVal = request.GET.get('upperVal', '')
    ward = Bride.objects.filter(price__range=(lowerVal, upperVal))
    return render(request, 'brands.html', {'ward': ward})


def products_details(request):
    productName = request.GET.get('productName', None)
    ward = Bride.objects.filter(name=productName)
    data = serializers.serialize('json', ward)
    return JsonResponse(data, safe=False)


def show_details(request):
    cart = CartCreate()
    if request.method == 'POST':
        cart = CartCreate(request.POST)
        if cart.is_valid():
            cart.save()
            return redirect('cart')
        else:
            return HttpResponse("Form not valid")
    else:
        cart.initial['user_id'] = request.user.id
        return render(request, 'productdetail.html', {'addcart_form': cart})


def cart(request):
    user_id = request.user.id
    user_cart = Cart.objects.filter(user_id=user_id)
    products = []
    for item in user_cart:
        product_cart = Bride.objects.filter(id=item.product_id)
        products.append(product_cart)
    return render(request, 'cart.html', {'products': products})


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

