from . views import *
from django.urls import path

urlpatterns = [
    path('Studenfunctionbasedtapi', StudentFunctionBasedAPI, name='Studenfunctionbasedtapi'),
]


