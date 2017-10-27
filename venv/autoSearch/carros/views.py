# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import car

# Creunate your views here.
def vista(recuest):
    return render(recuest, "home.html")

def car_list(request):
    carro = car.objects.all()
    contexto = {'contexto':carro}
    return render(request, "car_detail.html",contexto)
