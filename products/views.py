from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.
def by_product_single(request, id=None):
    product = get_object_or_404(Products, id=id)
    context = {'product': product}
    return render(request, 'single_product.html', context)