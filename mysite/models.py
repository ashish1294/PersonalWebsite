from django.db import models

# Create your models here.

#Class to Model Object
class project(models.Model):

    COURSE = 'course'
    EXTRA = 'extra'
    ONGOING = 'ongoing'
    STYLE_CHOICES = (
        (COURSE, 'Course Work'),
        (EXTRA, 'Extra Work'),
        (ONGOING, 'R'),
    )
    name = models.CharField(max_length = 200, unique = True)
    tag = models.CharField(max_length = 500)
    main_image = models.CharField(max_length = 200)
    main_image_caption = models.CharField(max_length = 400)
    folder = models.CharField(max_length = 200, unique = True)
    style = models.CharField(max_length = 200, choices = STYLE_CHOICES)
    alt_text = models.CharField(max_length = 500)
    link = models.CharField(max_length = 500)
    display_rank = models.IntegerField(default=1)

class message(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=25)
    checked = models.BooleanField(default=False)

class testimonial(models.Model):

    author = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    conection = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=25)
    content = models.TextField()
    approved = models.BooleanField(default=False)

class blog(models.Model):
    
    title = models.CharField(max_length=150)
    subtitle = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)

class normal_visit(models.Model):
    
    HOME_PAGE = 'home'
    PROFESSIAL_CAREER = 'prof_career'
    ACADEMIC_CAREER = 'acad_career'
    PORTOFOLIO = 'portofolio'
    CONTACT = 'contact'
    BLOG = 'blog'
    ACHIEVEMENTS = 'achievements'
    ABOUT_ME = 'about_me'
    SITE_MAP = 'sitemap'
    ADD_TESTIMONIAL = 'add_testimonial'
    
    visit_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=25)
    user_agent = models.TextField()
    page = models.CharField(max_length=20)
    
    @classmethod
    def new_visit(cls, ip_address, page, user_agent):
        record = normal_visit(ip=ip_address, page=page, user_agent=user_agent)
        record.save()
    
    @classmethod
    def unique_visit(cls, page):
        return normal_visit.objects.filter(page=page).values('ip').distinct().count()

class project_visit(models.Model):
    
    visit_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=25)
    user_agent = models.TextField()
    project = models.ForeignKey(project)

class blog_visit(models.Model):
    
    visit_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=25)
    user_agent = models.TextField()
    blog = models.ForeignKey(blog)

class error_404_visit(models.Model):
    
    visit_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=25)
    user_agent = models.TextField()
    url_requested = models.TextField()
    
    @classmethod
    def record_error(cls, ip_address, user_agent, url):
        record = error_404_visit(ip=ip_address, user_agent=user_agent, url_requested=url)
        record.save()