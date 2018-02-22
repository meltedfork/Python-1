# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import User

from django.contrib  import messages

def index(request):
    user = User.objects.all()
    context = {
        "users": user
    }
    return render (request, 'users/index.html',context)

def new(request):
    return render(request, 'users/new.html')
    
def edit(request, id):
    context = {

        "user": User.objects.get(id=int(id))
    }
    return render (request, "users/edit.html", context)
    
def show(request, id):
    context = {

        "user": User.objects.get(id=int(id))
    }
    return render (request, "users/show.html", context)
    
    
def create(request, methods="POST"):
    errors = User.objects.validation(request.POST)
    if len(errors) > 0:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('/new')
    User.objects.create(
        first = request.POST["first"],
        last = request.POST['last'],
        email = request.POST["email"],
    )
    user = User.objects.last()
    userid = user.id
    return redirect (str(userid)+'/show')
    
    
def destroy(request, id):
    User.objects.get(id=int(id)).delete()
    return redirect ('/')

def update(request,id):
    errors = User.objects.validation(request.POST)
    if len(errors) > 0:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect(id+'/edit')
    else:
        User.objects.filter(id=int(id)).update(first=request.POST['first'], last=request.POST['last'],email=request.POST["email"])
    return redirect ('/')

# Create your views here.