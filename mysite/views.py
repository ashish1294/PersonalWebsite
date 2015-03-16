from django.shortcuts import render
from mysite.models import *

# Create your views here.

def home(request) :
	return render(request, 'index.html', {'page' : 'home'})

def portofolio(request) :

	context = {
		'page' : 'portofolio',
		'project_list' : project.objects.all(),
	}

	return render(request, 'portofolio.html', context)

def add_stuff(request) :

	project.objects.all().remove()
	project_tab.objects.all().remove()

	p = project(name = '')
	p.tag = ""
	p.folder = ""
	p.main_image = ""
	p.style = project.COURSE
	p.alt_text = ""
	return "Added Stuff To Database Successfully"