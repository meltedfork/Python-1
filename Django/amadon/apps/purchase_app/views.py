# -*- coding: utf-8 -*-

#PRICE AND TOTAL NOT PULLING FROM HARD CODING METHOD. ASSIGNMENT UNFINISHED


from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    if "total" not in request.session:
        request.session["total"] = 0
    if "price" not in request.session:
        request.session["price"] = 0
    return render (request,'purchase/index.html')

def buy(request, methods="POST"):
    
    quantity = float(request.POST['quantity'])
    print quantity

    if request.POST["product_id"] == 1:
        price = 5.00 * quantity
        print price
    if request.POST["product_id"] == 2:
        price = 0.28 * quantity
        print price
    if request.POST["product_id"] == 3:
        price = 4000.00 * quantity
        print price
    
    quantity= int(quantity)
    request.session["total"] += request.session["price"]
    request.session["count"] += quantity
        
    return redirect('/checkout')
    

def checkout(request):
    return render (request, 'purchase/checkout.html')

def reset(request):
    request.session.clear()
    return redirect('/') 

# Create your views here.
