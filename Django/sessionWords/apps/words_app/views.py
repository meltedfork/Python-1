# -*- coding: utf-8 -*-

#UNFINISHED!!!!!!!!!!!!###
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime


def index(request):
    if "word" not in request.session:
        request.session["word"] = "test"
    if "color" not in request.session:
        request.session["color"] = "test"
    if "size" not in request.session:
        request.session["size"] = "p"
    if "queue" not in request.session:
        request.session["queue"] = []
    return render(request, 'words/index.html')

def add(request):
    request.session["word"] = request.POST["word"]
    request.session["color"]= request.POST["color"]

    if request.POST["size"] == "yes":
        request.session["size"] = True
    else:
        request.session["size"] = False

    context = {"size": request.session["size"]}
    
    miniDict = {"word": request.session["word"],
                "color": request.session["color"],
                "size": request.session["size"],
                "time": datetime.now().strftime("%Y/%m/%d %I:%M %p")
    }

    temp = []
    temp.append(miniDict)
    request.session["queue"] = temp
    return redirect('/')        

def clear(request):
    request.session.clear()

    return redirect ('/')
        
        
# Create your views here.