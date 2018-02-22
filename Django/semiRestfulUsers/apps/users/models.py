# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

import re
NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validation(self,postData):
        errors = {}
        if len(postData["first"]) < 2:
            errors["first"] = "First name must be greater than 2 characters!"
        elif not re.match(NAME_REGEX,postData["first"]):
            errors["first"] = "First name contains invalid characters."
        if len(postData["last"]) < 2:
            errors["last"] = "Last name must be greater than 2 characters!"
        elif not re.match(NAME_REGEX,postData["last"]):
            errors["last"] = "First name contains invalid characters."
        if len(postData["email"]) < 1:
            errors["email"] = "Email field cannot be blank!"
        elif not re.match(EMAIL_REGEX,postData["email"]):
            errors["email"] = "Email must be valid email."

        return errors

class User(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    objects = UserManager()
    

# Create your models here.
