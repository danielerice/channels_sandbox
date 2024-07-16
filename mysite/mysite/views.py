from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from table.models import Order

def home(request):
    return render(request, 'home.html')