from django.shortcuts import render
from .models import Order

def index(request):
    return render(request, 'index.html')

def add_order(request):
    if request.method == 'POST':
        # Save form data to the database
        pant_id = request.POST.get('pant_id')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        color = request.POST.get('color')
        size = request.POST.get('size')
        material = request.POST.get('material')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        order = Order(
            pant_id=pant_id,
            customer_name=customer_name,
            customer_email=customer_email,
            color=color,
            size=size,
            material=material,
            price=price,
            quantity=quantity
        )
        order.save()
    return render(request, 'index.html')

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})
