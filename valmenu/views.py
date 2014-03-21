from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Welcome to a better, simpler Valentine Menu, a venu, if you will.")
