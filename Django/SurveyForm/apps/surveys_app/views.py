# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    return render (request,"surveys/index.html")

def process(request, method="POST"):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comments"] = request.POST["comments"]
    request.session["count"] += 1
    return redirect ("/result")

def result(request):
    return render (request,"surveys/result.html")

def goback(request):
    return redirect('/')


# Create your views here.
