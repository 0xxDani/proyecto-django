from django.contrib import admin
from .models import Cart, Customer, OrderPlaced, Payment, Product, Wishlist, ContactMessage
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo_producto', 'precio_venta', 'precio_con_descuento', 'categoria', 'imagen_producto']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'direccion', 'telefono', 'ciudad', 'identificacion']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'productos', 'cantidad']
    
    def productos(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.titulo_producto)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'administradores', 'productos', 'cantidad', 'fecha_orden', 'pagos']
    
    def administradores(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.nombre)

    def productos(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.titulo_producto)

    def pagos(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'productos']
    
    def productos(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.titulo_producto)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'telefono', 'celular', 'identificacion', 'tipo_caso', 'asunto', 'numero_factura', 'descripcion']

admin.site.unregister(Group)
