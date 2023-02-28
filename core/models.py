from django.db import models
from django.contrib.auth import get_user_model 
#ready user model from django
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
    
#after create this,to find it from the admin panel i have to register it to admin .py

