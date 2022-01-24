from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
def hello(request):
    return  render(request,'enterprise_register/login.html')

