from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, 'shop/shop.html')
def shop(request):
    return render(request, 'shop/warenkorb.html')
def shop(request):
    return render(request, 'shop/kasse.html')