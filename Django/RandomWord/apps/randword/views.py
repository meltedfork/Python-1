# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index (request):
    if "random_word" not in request.session:
        request.session["random_word"] = ""
    if "counter" not in request.session:
        request.session["counter"]=0
    return render(request, 'randword/index.html')


def randomize(request):
    request.session["random_word"] = get_random_string(14)
    request.session["counter"] += 1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')