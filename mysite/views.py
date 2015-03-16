from django.shortcuts import render

# Create your views here.

def home(request) :
	return render(request, 'index.html', {'page' : 'home'})

def portofolio(request) :
	return render(request, 'portofolio.html', {'page' : 'portofolio'})

