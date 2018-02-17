# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from datetime import datetime
import random


def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "log" not in request.session:
        request.session["log"]=[]
    if "punish" not in request.session:
        request.session["punish"]=""
    return render (request,'gold/index.html')



def process(request, methods="POST"):
    
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    
    if request.POST["action"] == "farm":
        payout = random.randrange(10,21)
        request.session["gold"]+= payout
        request.session["log"].append(str(payout) +" Gold earned at the farm! " + time)

    elif request.POST["action"] == "cave":
        payout = random.randrange(5,10)
        request.session["gold"]+= payout
        request.session["log"].append(str(payout) +" Gold earned at the cave! " +time)

    elif request.POST["action"] == "house":
        payout = random.randrange(2,5)
        request.session["gold"]+= payout
        request.session["log"].append(str(payout) +" Gold earned house! " +time)

    elif request.POST["action"] == "casino":
        payout = random.randrange(-50,51)
        if payout >= 0:
            request.session["gold"]+= payout
            request.session["log"].append(str(payout) +" Gold earned at the casino! " +time)
        elif payout < 0:
            request.session["gold"]+= payout
            request.session["log"].append(str(payout) +" Gold lost at the casino! " +time)

    elif request.POST["action"] == "restart":
        request.session["gold"] = 0
        request.session["log"] = []

    if request.session["gold"] < 0:
        request.session["punish"] = "You can't pay your debts. Time to break your thumbs then."
    else:
        request.session["punish"] = ""

    return redirect ('/')


# Create your views here.
