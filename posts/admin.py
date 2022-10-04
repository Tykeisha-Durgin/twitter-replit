from django.contrib import admin

# Register your models here.
# here i import the model i have created
from .models import Post
admin.site.register(Post)