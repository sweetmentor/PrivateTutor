from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class Student(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    numbervalue = models.IntegerField(default=0, null=False)
    stringvalue = models.CharField(max_length=50, default='unknown', null = False, blank = False)
    
    # def __str__(self):
    #     return self.user.username
        
class Tutor(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor')
    verified = models.BooleanField(default=False)
    joined = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="avatars", null=False, default='no_image.jpg')
    description = models.TextField(max_length=50, default='unknown', null = False, blank = False)
    
    def __str__(self):
        return self.user.username