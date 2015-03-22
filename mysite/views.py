from django.shortcuts import render
from django.templatetags.static import static
from django.core.exceptions import ObjectDoesNotExist
from mysite.models import *
import os

# Create your views here.

#Function to handle the home-page
def home(request) :
    return render(request, 'index.html', {'page' : 'home'})

#Function to handle past-project page
def portofolio(request) :

    #Fetch all projects from database and load in context
    context = {
        'page' : 'portofolio',
        'project_list' : project.objects.all(),
    }

    return render(request, 'portofolio.html', context)

#Function to display project details
def project_handler(request, name) :

    #Fetch project details from database
    try :
        proj = project.objects.get(folder = name)

        images_folder = static('images/projects/' + name)

        images = []

        for image in os.listdir(images_folder) :
            images.append(os.path.join(images_folder, image))


        context = {
            'page' : 'portofolio',
            'project' : proj,
            'images' : images,
        }

        return render(request, name + '.html', context)

    except ObjectDoesNotExist :

        context = {
            'message' : '<h1>I have no knowledge about this project ! </h1> <h3 class="subheader"><a href="/portofolio">Click here</a> to view all my projects ! </h3>'
        }

        return render(request, 'error.html', context)

#View to handle Academic Career Page
def academic_career(request) :

    context = {
        'page' : 'career',
    }

    return render(request, 'academic_career.html', context)

def professional_career(request) :

    context = {
        'page' : 'career',
    }

    return render(request, 'professional_career.html', context)    

#View To Handle 404 Errors
def anything(request) :

    context = {
        'message' : '<h1>The page doesn\'t seem to exist !</h1>'
    }    
    return render(request, 'error.html', context)

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