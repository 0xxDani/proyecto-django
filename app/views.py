from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
import razorpay
from . models import Cart, Customer, OrderPlaced, Payment, Product, Wishlist, ContactMessage
from . forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

import uuid
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse

from django.template.defaultfilters import stringformat

def calculate_image_number(comment_content):
    return sum(ord(char) for char in comment_content)

def home(request):
    totalitem = 0
    wishitem = 0
    felicitaciones = ContactMessage.objects.filter(tipo_caso='felicitaciones')
    productos_recientes = Product.objects.order_by('-id')[:3]

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    context = {
        'felicitaciones': felicitaciones,
        'totalitem': totalitem,
        'wishitem': wishitem,
        'productos_recientes': productos_recientes,
    }

    return render(request, "app/home.html", context)

def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())


def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/contact.html",locals())

class CategoryView(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(categoria=val)
        titulo_producto = Product.objects.filter(categoria=val).values('titulo_producto')
        return render(request,"app/category.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(titulo_producto=val)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        titulo_producto = Product.objects.filter(categoria=product[0].categoria).values('titulo_producto')
        return render(request,"app/category.html",locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        wishlist = []

        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/customerregistration.html",locals())

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuario registrado exitosamente!")
        else:
            messages.warning(request,"Información inválida")
        return render(request, 'app/customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html',locals())

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            departamento = form.cleaned_data['departamento']
            ciudad = form.cleaned_data['ciudad']
            identificacion = form.cleaned_data['identificacion']

            reg = Customer(user=user,nombre=nombre,direccion=direccion,telefono=telefono,departamento=departamento,ciudad=ciudad,identificacion=identificacion)
            reg.save()
            messages.success(request,'Felicitaciones, perfil guardado con éxito')
        else:
            messages.warning(request,'Revise la información en los campos')
        return render(request, 'app/profile.html',locals())

@login_required
def address(request):
        add = Customer.objects.filter(user=request.user)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/address.html',locals())

@method_decorator(login_required,name='dispatch')
class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateAddress.html',locals())

    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.nombre = form.cleaned_data['nombre']
            add.direccion = form.cleaned_data['direccion']
            add.telefono = form.cleaned_data['telefono']
            add.departamento = form.cleaned_data['departamento']
            add.ciudad = form.cleaned_data['ciudad']
            add.identificacion = form.cleaned_data['identificacion']
            add.save()
            messages.success(request,'Felicitaciones, perfil actualizado correctamente')
        else:
            messages.warning(request,'Revisa bien todos los campos!')
        return redirect('address')

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.cantidad * p.product.precio_con_descuento
        amount = amount + value
    totalamount = amount + 2
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html',locals())

def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product= Wishlist.objects.filter(user=user)
    return render(request,"app/wishlist.html",locals())

@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.cantidad * p.product.precio_con_descuento
            famount = famount + value
        totalamount = famount + 2
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = { "amount": razoramount, "currency": "INR", "receipt": "order_rcptid_12" }
        payment_response = client.order.create(data=data)
        print(payment_response)
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()

        # Crear un nuevo formulario de PayPal con librería paypal-django
        host = request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': str(totalamount),
            'item_name': 'Producto',
            'invoice': str(uuid.uuid4()),
            'currency_code': 'USD',
            'notify_url': f'http://{host}{reverse("paypal-ipn")}',
            'return_url': f'http://{host}{reverse("paypal-return")}',
            'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
        }
        paypal_form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'app/checkout.html',locals())

def paypal_return(request):
    return redirect('orders')  

def paypal_cancel(request):
    messages.error(request, 'Tu pago no se realizó')
    return redirect('checkout')  

@login_required
def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')

    user=request.user
    customer=Customer.objects.get(id=cust_id)

    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,cantidad=c.cantidad,payment=payment).save()
        c.delete()
    return redirect("orders")

@login_required
def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    order_placed=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.cantidad+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.cantidad * p.product.precio_con_descuento
            amount = amount + value
        totalamount = amount + 2
        # print(prod_id)
        data={
            'cantidad': c.cantidad,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.cantidad-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.cantidad * p.product.precio_con_descuento
            amount = amount + value
        totalamount = amount + 2
        # print(prod_id)
        data={
            'cantidad': c.cantidad,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.cantidad * p.product.precio_con_descuento
            amount = amount + value
        totalamount = amount + 2
        # print(prod_id)
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save()
        data={
            'message': 'Añadido a la lista de favoritos',
        }
        return JsonResponse(data)

def minus_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data={
            'message': 'Eliminado de la lista de favoritos',
        }
        return JsonResponse(data)

def search(request):
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(Q(titulo_producto__icontains=query))
    return render(request,"app/search.html", locals())

def contact(request):
    if request.method == 'POST':
        # Recuperar datos del formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        celular = f"{request.POST.get('indicativo')}{request.POST.get('celular')}"
        identificacion = request.POST.get('identificacion')
        tipo_caso = request.POST.get('tipo-caso')
        asunto = request.POST.get('asunto')
        numero_factura = request.POST.get('numero-factura')
        descripcion = request.POST.get('descripcion')

        # Guardar en la base de datos
        mensaje = ContactMessage(
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            celular=celular,
            identificacion=identificacion,
            tipo_caso=tipo_caso,
            asunto=asunto,
            numero_factura=numero_factura,
            descripcion=descripcion
        )
        mensaje.save()

        # Devolver una respuesta JSON
        return JsonResponse({'status': 'success'})

    return render(request, 'app/contact.html')