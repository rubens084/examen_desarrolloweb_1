# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import car
from django.views.generic import DetailView,ListView ,CreateView

# Creunate your views here.
def vista(recuest):
    return render(recuest, "home.html")

class car_list(ListView):
    template_name='car_list.html'
    queryset=car.objects.all()

class car_detail(DetailView):
    template_name='car_detail.html'
    queryset= car.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return car.objects.get(id=id)
