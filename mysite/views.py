from django.shortcuts import render
from django.templatetags.static import static
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from mysite.models import project, message
import os

# Create your views here.
project 

#Function to handle the home-page
def home(request):
    return render(request, 'index.html', {'page' : 'home'})

#Function to handle past-project page
def portofolio(request):

    #Fetch all projects from database and load in context
    context = {
        'page' : 'portofolio',
        'project_list' : project.objects.all(),
    }

    return render(request, 'portofolio.html', context)

#Function to display project details
def project_handler(request, name):

    #Fetch project details from database
    try:
        proj = project.objects.get(folder = name)

        images_folder = static('images/projects/' + name)

        images = []

        for image in os.listdir(images_folder):
            images.append(os.path.join(images_folder, image))


        context = {
            'page' : 'portofolio',
            'project' : proj,
            'images' : images,
        }

        return render(request, name + '.html', context)

    except ObjectDoesNotExist:

        context = {
            'message' : '<h1>I have no knowledge about this project ! </h1> <h3 class="subheader"><a href="/portofolio">Click here</a> to view all my projects ! </h3>'
        }

        return render(request, 'error.html', context)

#View to handle Academic Career Page
def academic_career(request):

    sgpa = [9.32, 9.45, 9.83, 9.55, 9.20, 9.48]
    credits = [21, 20, 24, 23, 25, 23]

    semwise = []
    for i, x in enumerate(sgpa):
        temp = []
        temp.append(sgpa[i])
        temp.append(credits[i])
        semwise.append(temp)

    course_left = [
        'IT 200 - Data Structures and Algorithms',
        'IT 201 - Digital Design and Computer Organization',
        'IT 202 - Unix Programming and Practice',
        'IT 203 - Computer Systems and Organization Lab',
        'IT 204 - Data Structures and Algorithms Lab',
        'IT 206 - Paradigms of Programming Part I',
        'MA 200 - Graph Theory, Probability and Statistics',
        'IT 250 - Operating Systems',
        'IT 251 - Computer Communication and Networking',
        'IT 252 - Design and Analysis of Algorithms',
        'IT 253 - Paradigms of Programming Part II',
        'IT 254 - Computer Graphics',
        'IT 306 - Object Oriented Analysis and Design',
        'IT 290 - Seminar'
    ]

    course_right = [
        'HU 300 - Engineering Economics',
        'IT 300 - Parallel Computing',
        'IT 301 - Database Systems',
        'IT 302 - Web Technologies and Applications',
        'IT 303 - Automata and Compiler Design',
        'IT 307 - Advance Computer Networks',
        'IT 360 - Distributed Computing System',
        'IT 350 - Software Engineering',
        'HU 302 - Principles of Management',
        'MA 204 - Linear Algebra anf Matrices',
        'IT 351 - Human Computer Interaction',
        'IT 352 - Information Assurance and Security',
        'IT 399 - Minor Project',
        'IT 450 - Web Services'
    ]

    context = {
        'page' : 'career',
        'semwise' : semwise,
        'cgpa' : 9.47,
        'course_left' : course_left,
        'course_right' : course_right
    }

    return render(request, 'academic_career.html', context)

def professional_career(request):

    context = {
        'page' : 'career',
    }

    return render(request, 'professional_career.html', context)    

#View To Handle 404 Errors
def anything(request):

    context = {
        'message' : '<h1>The page doesn\'t seem to exist !</h1>'
    }    
    return render(request, 'error.html', context)

#View to draw Sunburst of skills
def skill_chart(request):

    return render(request, 'sunburst.html', {})

#View to Render the Blog
def blog(request):

    return render(request, 'blog.html', {})

#Function to get IP Address of the request
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#View to handle the contact page
def contact(request):

    context = {}

    if 'submit' in request.POST:
        msg = message(name=request.POST['name'], email=request.POST['email'], message=request.POST['message'], ip=get_client_ip(request))
        msg.save()
        context.update({'message' : 'Your message was recorded ! You will hear from me ASAP :)', 'messagetype' : 'success'})

    context.update(csrf(request))
    return render(request, 'contact.html', context)

def add_stuff(request):

    project.objects.all().remove()

    p = project(name = '')
    p.tag = ""
    p.folder = ""
    p.main_image = ""
    p.style = project.COURSE
    p.alt_text = ""
    return HttpResponse("Added Stuff To Database Successfully")