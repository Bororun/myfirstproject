from django.http import	HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('Hello Polina. This is about this site.')

def home(request):
	return render(request, 'home.html', {'greeting':'Hello!'})