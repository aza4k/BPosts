from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	number = models.CharField(max_length=15,blank=True, null=True)
	image = models.ImageField(upload_to='profile_img', null=True,default='image-2282302_960_720.png')