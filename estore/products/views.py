from django.shortcuts import render

from products.models import Product, Category


def index(request):
    products = Product.objects.all()[:8]
    return render(
        request,
        "products/index.html",
        {"products": products},
    )


def product(request, slug: str):
    product = Product.objects.get(slug=slug)
    return render(
        request,
        "products/product.html",
        {"product": product},
    )


def category(request, slug: str):
    category = Category.objects.get(slug=slug)
    return render(
        request,
        "products/category.html",
        {"category": category},
    )
