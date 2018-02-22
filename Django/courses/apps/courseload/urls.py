from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>\d+)/delete$', views.delete, name="delete"),     
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name="destroy"),     
    url(r'^add$', views.add, name = "add"),
    url(r'^(?P<id>\d+)/profile$', views.profile, name = "profile"),         
    url(r'^(?P<id>\d+)/addfave$', views.addfave, name = "addfave"),         
    url(r'^(?P<id>\d+)/unfave$', views.unfave, name = "unfave"),         
         
  ]