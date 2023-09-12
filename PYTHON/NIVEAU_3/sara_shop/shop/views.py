from django.shortcuts import render, redirect
from .models import Dish, Order, Beverage, Sauce

def index(request):
    dishes = Dish.objects.all()
    sauces = Sauce.objects.all()
    beverages = Beverage.objects.all()
    return render(request, 'index.html', {'dishes': dishes, 'sauces': sauces, 'beverages': beverages})

def create_order(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish')
        customer_name = request.POST.get('customer_name')
        dish = Dish.objects.get(id=dish_id)

        sauce_id = request.POST.get('sauce')
        if sauce_id:
            sauce = Sauce.objects.get(id=sauce_id)
        else: sauce = None

        beverage_id = request.POST.get('beverage')
        if beverage_id:
            beverage = Beverage.objects.get(id=beverage_id)
        else:
            beverage = None

        new_order = Order(dish=dish, sauce=sauce, beverage=beverage, customer_name=customer_name, processed=False)
        new_order.save()
        return redirect('index')
    dishes = Dish.objects.all()
    sauces = Sauce.objects.all()
    beverages = Beverage.objects.all()
    return render(request, 'create_order.html', {'dishes': dishes, 'sauces': sauces, 'beverages': beverages})

def filter_orders(request):
    if request.method == 'GET':
        status = True if request.GET.get('status') == 'processed' else False
        customer_name = request.GET.get('customer_name')
        
        orders = Order.objects.all()
        
        if status:
            orders = Order.objects.all().filter(processed=status)
        if customer_name:
            orders = Order.objects.all().filter(customer_name__icontains=customer_name)
            
        return render(request, 'filter_orders.html', {'dishes': Dish.objects.all(), 'orders': orders})

