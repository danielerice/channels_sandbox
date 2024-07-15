from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from table.models import Order


def index(request):
    return HttpResponse("Hello, world. You're at the table index.")

@csrf_exempt
def orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        return HttpResponse(orders)
    if request.method == 'POST':
        return HttpResponse(request.POST)
    return HttpResponse("nah")