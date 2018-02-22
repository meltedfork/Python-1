# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *

from ..login_app.models import *

from django.contrib import messages


def index(request):
    course = Course.objects.all()
    context = {
        "courses": course
    }
    return render (request, "courseload/index.html", context)

def delete(request, id):
    context = {

        "course": Course.objects.get(id=id)
    }

    return render (request, "courseload/delete.html", context)

def destroy(request, id):
    Course.objects.get(id=int(id)).delete()
    return redirect (reverse('courses:index'))   #redirect to a reverse method that takes you to the named route

def add(request):
    
    errors = Course.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect (reverse('courses:index'))

    Course.objects.create(name = request.POST["name"], desc = request.POST["desc"])   #set course to a query
    # Description.objects.create(desc=request.POST["desc"], course=course)   #create() pushes to DB

    return redirect (reverse('courses:index'))

def profile(request, id): 
    currentUser = User.objects.get(id=id)
    faves=currentUser.userfaves.all()

    context = {

        "favorites": faves
    }
    
    return render (request, "courseload/profile.html", context)

def addfave(request, id):
    currentUser = User.objects.get(id=request.session['userid'])  #grab object of current user via current user id
    fave = Course.objects.get(id=id)        #grab object of specific course id
    fave.favorites.add(currentUser)
    
    return redirect (reverse('courses:profile', args=(currentUser.id,)))  #args is to grab the current user id. the comma after is NECESSARY in a one item tuple
    

def unfave (request, id):
    currentUser = User.objects.get(id=request.session['userid'])  #grab object of current user via current user id
    fave = Course.objects.get(id=id)        #grab object of specific course id
    fave.favorites.remove(currentUser)

    return redirect (reverse('courses:profile', args=(currentUser.id,)))
# Create your views here.
