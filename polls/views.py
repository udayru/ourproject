from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("hello world you are the polls index")
	

# Create your views here.
