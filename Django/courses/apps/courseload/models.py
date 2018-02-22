# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..login_app.models import *

from datetime import date


class CourseManager(models.Manager):
    def validate (self,data):
        errors ={}
        if len(data["name"]) < 5:
            errors["name"] = "Course name must be more than 5 characters."
        if len(data["desc"]) < 15:
            errors["desc"] = "Course description must be more than 15 characters."
        
        return errors
        


class Course(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=75)
    favorites = models.ManyToManyField(User, related_name="userfaves")
    created = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()

# class Description(models.Model):
#     desc = models.CharField(max_length=75)
#     course = models.OneToOneField(Course, related_name="descriptions")
#     objects = CourseManager()

# class Favorite(models.Model):
#     favorite = models.CharField(max_length=20)
#     userFavorites = models.ManyToManyField(Course,)
#     created = models.DateTimeField(auto_now_add=True)
#     objects = CourseManager()

# Create your models here.
