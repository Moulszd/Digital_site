from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    
    return render(request,'digitalapp/index.html',{'products':products})


def detail(request,id):
    product = Product.objects.get(id=id)
    # stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'digitalapp/detail.html',{'product':product,
    # 'stripe_publishable_key':stripe_publishable_key
    })
    