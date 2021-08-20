from typing import ValuesView
from django.urls import path
from . import views

app_name="hello"
urlpatterns = [
    path("", views.index, name="index" ),
    path("kushal", views.kushal,name="kushal"),
    path("david",views.david,name="david"),
    path('add/',views.add,name="add"),
    path("<str:name>",views.greets,name="greets")
]