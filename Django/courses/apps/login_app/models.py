# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..courseload.models import *

from datetime import datetime
import bcrypt

import re
NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def validation(self,postData):
        errors = {}
        if len(postData["first"]) < 2:
            errors["first"] = "First name must be greater than 2 characters!"
        elif not re.match(NAME_REGEX,postData["first"]):
            errors["first"] = "First name contains invalid characters or spaces."
        if len(postData["last"]) < 2:
            errors["last"] = "Last name must be greater than 2 characters!"
        elif not re.match(NAME_REGEX,postData["last"]):
            errors["last"] = "Last name contains invalid characters or spaces."
        if len(postData["email"]) < 1:
            errors["email"] = "Email field cannot be blank!"
        elif not re.match(EMAIL_REGEX,postData["email"]):
            errors["email"] = "Email must be valid email."
        elif User.objects.filter(email = postData["email"]).count() > 0:
            errors["email"] = "Email address already exists. Please choose another."
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        if postData["confirm"] != postData["password"]:
            errors["confirm"] = "Passwords do not match!"

        return errors

    def logvalidate(self, postData):
        errors={}
        if User.objects.filter(email=postData["email"]):   #query to find if any email matches POST
            currentUser = User.objects.get(email=postData["email"])  #currentUser set to that object
            tempPW = currentUser.password       #tempPW becomes currentUSER password
            if not bcrypt.checkpw(postData["password"].encode(), tempPW.encode()):  #if the hashed password doesn't match the stored hashed pw
                errors["password"] = "Invalid password."
        else:
            errors["email"] = "Email address does not exist in database"
        return errors

class User(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # confirm = models.CharField(max_length=20)  not needed!

    objects = UserManager()
    

# Create your models here.
