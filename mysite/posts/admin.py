from django.contrib import admin
from .models import Post, Comment

admin.site.site_header = "mysite Admin"
admin.site.site_title = "mysite Admin Area"
admin.site.index_title = "Welcome to the mysite admin area"

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)