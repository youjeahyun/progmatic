from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request): #뷰함수명
    return HttpResponse("안녕하세요!")