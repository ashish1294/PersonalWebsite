from django.db import models

# Create your models here.

#Class to Model Object
class project(models.Model) :

	COURSE = 'course'
	EXTRA = 'extra'
	RESEARCH = 'research'
	STYLE_CHOICES = (
		(COURSE, 'Course Work'),
		(EXTRA, 'Extra Work'),
		(RESEARCH, 'RESEARCH'),
	)
	name = models.CharField(max_length = 200, unique = True)
	tag = models.CharField(max_length = 500)
	description = models.TextField()
	main_image = models.CharField(max_length = 200)
	main_image_caption = models.CharField(max_length = 400)
	folder = models.CharField(max_length = 200, unique = True)
	style = models.CharField(max_length = 200, choices = STYLE_CHOICES)
	alt_text = models.CharField(max_length = 500)
	link = models.CharField(max_length = 500)

#Class to Model Tab section of each project
class project_tab(models.Model) :
	proj = models.ForeignKey(project)
	name = models.CharField(max_length = 200)
	description = models.TextField()