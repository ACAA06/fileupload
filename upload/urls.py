from django.urls import path

from . import views

urlpatterns = [path("", views.getquote, name="getquote"),
path("upload", views.upload, name="upload"),
               ]