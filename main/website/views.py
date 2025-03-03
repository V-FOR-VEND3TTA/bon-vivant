from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def cart(request):
    return render(request, 'website/cart.html')

def checkout(request):
    return render(request, 'website/checkout.html')

def contact(request):
    return render(request, 'website/contact.html')

def shop(request):
    return render(request, 'website/shop.html')

def thank_you(request):
    return render(request, 'website/thankyou.html')
