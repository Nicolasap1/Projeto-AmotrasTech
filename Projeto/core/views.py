from django.shortcuts import render

def index(request):
    """Pagina Principal"""
    return render(request, 'core/index.html')

def login(request):
    """Pagina de Login"""
    return render(request, 'core/login.html')

def category(request):
    """Pagina de Categorias"""
    return render(request, 'core/category.html')

def cart(request):
    """Pagina de Carrinho"""
    return render(request, 'core/cart.html')

def description(request):
    """Pagina de Descrição"""
    return render(request, 'core/description.html')

def promo(request):
    """Pagina de Descrição"""
    return render(request, 'core/promo.html')