from django.db import models

#A blog model object for admin site


class Blog(models.Model):
	title = models.CharField(max_length=40, help_text = 'Enter the title of blog')
	pub_date = models.DateField(auto_now_add=True, blank=False)
	text = models.TextField(max_length=3000, help_text= "Enter the text")
	blog_image = models.ImageField(upload_to='images/')

