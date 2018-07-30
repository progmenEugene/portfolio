from django.db import models



#model object for admin site and database
class Job(models.Model):
	image = models.ImageField(upload_to = 'images/')
	summary = models.CharField(max_length=300, help_text = 'Enter your summary')

	

