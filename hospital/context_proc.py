from .models import ProductCategory, Order

def get_some_context(request):
    get_categories = ProductCategory.objects.all()
    context = {
        'get_categories': get_categories,
    }
    return context

def get_order_number(request):
    if request.user.is_authenticated:
        product_count = Order.objects.filter(user=request.user).count()
    else:
        product_count = 0

    context = {
        'product_count': product_count
    }

    return context