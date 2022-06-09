
from distutils.util import change_root
from locale import currency
from re import template
from urllib.request import Request
from venv import create
from django.shortcuts import render,get_object_or_404,redirect
from django.template import context
from django.views.generic import View
from .models import Item,OrderItem,Order,Payment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
import stripe
from django.conf import settings


class IView(View):
    def get(self,request,*args, **kwargs):
        item_data=Item.objects.all()
        return render(request,'EC/EC.html',{
            'item_data':item_data
        })

class ItemDetailView(View):
    def get(self,request,*args, **kwargs):
        item_data=Item.objects.get(id=self.kwargs['pk'])
        return render(request,'EC/product.html',{
            'item_data':item_data
        })


@login_required
def addItem(request,pk):
    item=get_object_or_404(Item,pk=pk)
    order_item,created=OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order=Order.objects.filter(user=request.user,ordered=False)

    if order.exists():
        order=order[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order=Order.objects.create(user=request.user,ordered_date=timezone.now())
        order.items.add(order_item)
    return redirect('order')

class OrderView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        try:
            order=Order.objects.get(user=request.user,ordered=False)
            context={
                'order':order
            }
            return render(request,'EC/order.html',context)
        except ObjectDoesNotExist:
            return render(request,'EC/order.html')

@login_required
def removeItem(request,pk):
    item=get_object_or_404(Item,pk=pk)
    order=Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order.exists():
        order=order[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect('order')
    return redirect('product',pk=pk)

@login_required
def removesingleItem(request,pk):
    item=get_object_or_404(Item,pk=pk)
    order=Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order.exists():
        order=order[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity>1:
                order_item.quantity-=1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
            return redirect('order')
    return redirect('product',pk=pk)


class PaymentView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        order=Order.objects.get(user=request.user,ordered=False)
        user_data=CustomUser.objects.get(id=request.user.id)
        context={
            'order':order,
            'user_data':user_data
        }
        return render(request,'EC/payment.html',context)
    def post(self,request, *args, **kwargs):
        order=Order.objects.get(user=request.user,ordered=False)
        order_items=order.items.all()
        amount=order.get_total()

        payment=Payment(user=request.user)
        payment.stripe_charge_id='test_stripe_charge_id'
        payment.amount=amount
        payment.save()

        order_items.update(ordered=True)
        for item in order_items:
            item.save()
        order.ordered=True
        order.payment=payment
        order.save()
        return redirect('thanks')


class ThanksView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        
        return render(request,'EC/thanks.html')