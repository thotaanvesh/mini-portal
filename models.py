from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    image=models.ImageField(upload_to='images')
    author=models.ForeignKey(User,on_delete=models.CASCADE)

