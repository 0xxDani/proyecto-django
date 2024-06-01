from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    # path('favicon.ico', lambda x: HttpResponseNotFound()),
]
