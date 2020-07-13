from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customer,Product,Tag,Order
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()

    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status="Delivered").count()
    pending=orders.filter(status="Pending").count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()

    order_count=orders.count()
    return render(request,'accounts/customer.html',{'customer':customer,'orders':orders,'order_count':order_count}) 

class CreateOrder(CreateView):
    model=Order
    fields=['customer','product','status']

class UpdateOrder(UpdateView):
    model=Order
    fields= ['customer','product','status']      

class DeleteOrder(DeleteView):  
     model=Order
     success_url=reverse_lazy('accounts:home')