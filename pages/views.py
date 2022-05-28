import pytz
from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView
from django.db.models.query_utils import Q

from product.models import Product
from pages.models import(
    Advertisement,
    OtherProducts,
    TopBanner
)


class Home(ListView):
    def get(self,request):
        other_products=OtherProducts.objects.first().products.all().order_by('date_create')[:50]
        products=Product.objects.all().order_by('date_create')[:12]
        ads= Advertisement.objects.filter(Q(publication_date_start__lte=pytz.UTC.localize(datetime.now())) & Q(publication_date_end__gte=pytz.UTC.localize(datetime.now())))
        banners= TopBanner.objects.filter(is_active=True)
        context = { 
            'other_products':other_products,
            'products':products,
            'ads':ads,
            'banners':banners
        }
        return render(request , 'home.html' ,context)