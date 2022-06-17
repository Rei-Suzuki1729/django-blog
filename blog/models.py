from distutils.command.upload import upload
from turtle import title, update
from django.db import models


class Post(models.Model):
  title = models.CharField(max_length=100)
  content =models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  is_published = models.BooleanField(default=False)
  image = models.ImageField(upload_to="uploads/",null=True,blank=True )

def _str_(self):
  return self.title
