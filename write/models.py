from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import pickle




class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Write(models.Model):
    id = models.BigAutoField(primary_key=True)
    pub_date = models.DateTimeField(null=False, auto_now_add=True)
    title = models.TextField(null = True)
    things = models.TextField(null = True)


    def __str__(self):
        return self.title



class Photo(models.Model):
    write_id = models.IntegerField(null=False)
    pub_date = models.DateTimeField(null=False, auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
