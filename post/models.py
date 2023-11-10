from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	image = models.ImageField(upload_to='posts/%Y/%m/%d')
	description = models.TextField()
	aviable = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	author = models.CharField(max_length=255, blank=True,null=True)

	def __str__(self):
		return self.title
