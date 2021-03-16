from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from .decorators import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.


@unauthicated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'crm1/signin.html', context)


def signout(request):
    logout(request)
    return redirect("login")



def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            #logic implemented by signals

            messages.success(request, username + " Successfully created")
            return redirect("login")

    context = {"form": form}
    return render(request, 'crm1/signup.html', context)


# <--- Updated with Customer data -->

# @login_required(login_url='login')
# @allowed_users('customer')
# def user_page(request):
#     orders= request.user.customer.order_set.all()
#     total_orders = orders.count()
#     pending_orders = orders.filter(status="Pending").count()
#     delivered_orders = orders.filter(status="Delivered").count()
#     context = {'order': orders,
#                 "total": total_orders,
#                "pending": pending_orders,
#                "delivered": delivered_orders,
#                 }
#     return render(request, 'crm1/user_details.html', context)


@login_required(login_url='login')
@admin_only
def dashboard(request):

    customers = Customer.objects.all()
    orders = Order.objects.order_by('date_created')
    order_latest= orders[:5]
    total_orders = orders.count()
    pending_orders = orders.filter(status="Pending").count()
    delivered_orders = orders.filter(status="Delivered").count()

    context = {"customers": customers, "orders": orders,
               "total": total_orders,
               "pending": pending_orders,
               "delivered": delivered_orders,
               "order_latest":order_latest,
               }

    return render(request, 'crm1/dashboard.html', context)


@login_required(login_url='login')
def product(request):

    products = Product.objects.all()
    return render(request, 'crm1/product.html', {"products": products})


@login_required(login_url='login')
def customer(request, pk):

    req_customer = Customer.objects.get(id=pk)
    order = req_customer.order_set.all()
    orderfilter = OrderFilter(request.GET, queryset=order)
    order = orderfilter.qs
    total_count = order.count()

    context = {"customer": req_customer, "order": order, "count": total_count,
               "orderfilter": orderfilter}
    return render(request, 'crm1/customer.html', context)


@login_required(login_url='login')
def create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    order = OrderForm(initial={'customer': customer})
    if request.method == "POST":
        order = OrderForm(request.POST)
        if order.is_valid():
            order.save()
            return redirect('customer', pk)

    context = {"form": order}
    return render(request, 'crm1/create_order.html', context)


@login_required(login_url='login')
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    order_form = OrderForm(instance=order)
    if request.method == "POST":
        order = OrderForm(request.POST, instance=order)
        if order.is_valid():
            order.save()
            return redirect('/')

    context = {"form": order_form}

    return render(request, 'crm1/update_order.html', context)


@login_required(login_url='login')
def remove_order(request, pk):
    order = Order.objects.get(id=pk)

    context = {"item": order}

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'crm1/remove_order.html', context)


@login_required(login_url='login')
@allowed_users(['customer'])
def account_setting(request):
    customer= request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context ={'form': form}
    return render(request, 'crm1/account_setting.html', context)

@login_required(login_url='login')
@allowed_users('admin')
def orders(request):
    orders = Order.objects.all()
    orderfilter = OrderFilterAll(request.GET , queryset=orders)
    orders = orderfilter.qs
    context ={'orders':orders,
            'orderfilter':orderfilter,
            }

    return render(request, 'crm1/orders.html', context)

