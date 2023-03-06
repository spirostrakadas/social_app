from django.db import models
from django.contrib.auth import get_user_model 
#ready user model from django
import uuid
from datetime import datetime
#when you create a table an you want to see it in the admin panel you hate to register it at admin.py
User=get_user_model() 

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(max_length=200,blank=True)
    profile_img=models.ImageField(upload_to='profile_images',default='blank_prof_image.png')
    location= models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.user.username
    
#after i create this table,to find it from the admin panel in my site i have to register it to admin .py

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    caption=models.TextField(max_length=300)
    created_at=models.DateTimeField(default=datetime.now)
    number_of_likes=models.IntegerField(default=0)


    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    
    def __str__(self):
        return self.username