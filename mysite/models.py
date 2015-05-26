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

class message(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=500)
	message = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	ip = models.CharField(max_length=25)
	checked = models.BooleanField(default=False)