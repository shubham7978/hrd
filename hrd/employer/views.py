from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return HttpResponse("Hello,world. This is the employer view.")
# Create your views here.
