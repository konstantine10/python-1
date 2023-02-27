from django.db import models

class Book (models.Model):
    title=models.CharField(default="title",max_length=100)
    author=models.CharField(default="author",max_length=50)
    pages_count=models.IntegerField(default=0)



