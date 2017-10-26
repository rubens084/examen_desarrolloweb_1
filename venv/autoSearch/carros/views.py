# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Creunate your views here.
def vista(recuest):
    return render(recuest, "home.html")
