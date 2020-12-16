from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200, default="")
    body= models.TextField(default="")

    pub_data= models.DateTimeField("publish date", default=timezone.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(default="")
    likes = models.IntegerField(default=0)

    post=models.ForeignKey('Post', on_delete=models.CASCADE,)

    def __str__(self):
        return self.text