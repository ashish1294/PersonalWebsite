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

    #Fetch project details and it's tabs from database
    try :
        proj = project.objects.get(folder = name)
        tabs = project_tab.objects.filter(proj = proj)
        print "Tabs = ", tabs

        images_folder = static('images/projects/' + name)

        images = []

        for image in os.listdir(images_folder) :
            images.append(os.path.join(images_folder, image))


        context = {
            'page' : 'portofolio',
            'project' : proj,
            'tabs' : tabs,
            'images' : images,
        }

        return render(request, 'project.html', context)

    except ObjectDoesNotExist :

        context = {
            'message' : 'I have no knowledge about the project you are looking for !'
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