from django.contrib import admin
from .models import *

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
	pass
