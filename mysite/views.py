from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.conf import settings
from mysite.models import project, message, normal_visit, project_visit,\
  error_404_visit, testimonial
import os

#Function to get IP Address of the request
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
  
def record_visit(request, page):
    normal_visit.new_visit(get_client_ip(request), page, request.META.get('HTTP_USER_AGENT'))
    return normal_visit.unique_visit(page)
  
def site_map(request):
    return render(request, 'sitemap.xml', {}, content_type='text/xml')

def search(request) :
    print "Rendering Search"  
    return render(request, 'search.html', {})
#Function to handle the home-page
def home(request):

    context = {
        'page' : 'home',
        'visitors' : record_visit(request, normal_visit.HOME_PAGE),
        'testimonial_list' : testimonial.objects.filter(approved=True),
    }

    return render(request, 'index.html', context)

#Function to handle past-project page
def portofolio(request):

    #Fetch all projects from database and load in context
    context = {
        'page' : 'portofolio',
        'project_list' : project.objects.all(),
        'visitors' : record_visit(request, normal_visit.PORTOFOLIO)
    }

    return render(request, 'portofolio.html', context)

#Function to display project details
def project_handler(request, name):

    #Fetch project details from database
    try:
        proj = project.objects.get(folder = name)
        temp = os.path.join(os.path.join(settings.STATICFILES_DIRS[0], 'images'), 'projects')
        images_folder = os.path.join(temp, name)

        images = []

        for image in os.listdir(images_folder):
            images.append('images/projects/' + name + '/' + image)
            print 'images/projects/' + name + '/' + image

        vis = project_visit(ip=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT'), project=proj)
        vis.save()
        
        context = {
            'page' : 'portofolio',
            'project' : proj,
            'images' : images,
            'visitors' : project_visit.objects.filter(project=proj)
                .values('ip').distinct().count()
        }

        return render(request, name + '.html', context)

    except ObjectDoesNotExist:
        
        error_404_visit.record_error(get_client_ip(request),
            request.META.get('HTTP_USER_AGENT'),'project/' + name)
        
        context = {
            'message' : '''<h1>I have no knowledge about this project ! </h1>
                <h3 class="subheader"> <a href="/portofolio">Click here</a>
                to view all my projects ! </h3>''',
            'visitors' : 'Error'
        }

        return render(request, 'error.html', context)

#View to handle Academic Career Page
def academic_career(request):

    sgpa = [9.32, 9.45, 9.83, 9.55, 9.20, 9.48]
    credit_list = [21, 20, 24, 23, 25, 23]

    semwise = []
    for i in range(len(sgpa)):
        temp = []
        temp.append(sgpa[i])
        temp.append(credit_list[i])
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
        'course_right' : course_right,
        'visitors' : record_visit(request, normal_visit.ACADEMIC_CAREER)
    }

    return render(request, 'academic_career.html', context)

def professional_career(request):

    context = {
        'page' : 'career',
        'visitors' : record_visit(request, normal_visit.PROFESSIAL_CAREER)
    }

    return render(request, 'professional_career.html', context)

#View To Handle 404 Errors
def anything(request, path):

    error_404_visit.record_error(get_client_ip(request), request.META.get('HTTP_USER_AGENT'), path)
    
    context = {
        'message' : '<h1>The page doesn\'t seem to exist !</h1>',
        'visitors' : 'Error'
    }    
    return render(request, 'error.html', context)

#View to draw Sunburst of skills
def skill_chart(request):
    return render(request, 'sunburst.html', {})

#View to Render the Blog
def blog(request):

    context = {
        'visitors' : record_visit(request, normal_visit.BLOG),
        'page' : 'blog'
    }
    return render(request, 'blog.html', context)

#View to handle the contact page
def contact(request):

    context = {
        'visitors' : record_visit(request, normal_visit.BLOG),
        'page' : 'contact'
    }

    if 'submit' in request.POST:
        msg = message(name=request.POST['name'], email=request.POST['email'],
            message=request.POST['message'], ip=get_client_ip(request))
        msg.save()
        context.update({'message' : 'Your message was recorded ! You will hear from me ASAP :)', 'messagetype' : 'success'})

    context.update(csrf(request))
    return render(request, 'contact.html', context)

def about_me(request):
    
    return render(request, 'aboutme.html', {
        'visitors' : record_visit(request, normal_visit.ABOUT_ME),
        'page' : 'aboutme'
    })

def achievement(request):
    
    return render(request, 'achievements.html', {
        'visitors': record_visit(request, normal_visit.ACHIEVEMENTS),
        'page' : 'achievements'
    })

def add_testimonial(request):

    context = {
        'visitors' : record_visit(request, normal_visit.ADD_TESTIMONIAL),
    }
    context.update(csrf(request))

    if 'submit' in request.POST:
        test = testimonial(
            author = request.POST['author'],
            email = request.POST['email'],
            conection = request.POST['connection'],
            ip = get_client_ip(request),
            content = request.POST['content']
        )

        test.save()
        context.update({'message' : 'Your Testmonial has been successfully submitted for Approval !'})

    return render(request, 'add_testimonial.html', context)

def add_stuff(request):

    project.objects.all().remove()

    p = project(name = '')
    p.tag = ""
    p.folder = ""
    p.main_image = ""
    p.style = project.COURSE
    p.alt_text = ""
    return HttpResponse("Added Stuff To Database Successfully")