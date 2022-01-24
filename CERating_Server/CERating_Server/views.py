from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
def hello(request):
    return  render(request,'enterprise_register/login.html')

