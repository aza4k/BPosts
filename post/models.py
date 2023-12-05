from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='posts/%Y/%m/%d')
	description = RichTextField(config_name='awesome_ckeditor')	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

	def __str__(self):
		return self.title
