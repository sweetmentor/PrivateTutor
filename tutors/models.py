from django.db import models
from subjects.models import Subjects
# Create your models here.

class Tutor(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=50, default='unknown', null = False, blank = False)
    image = models.ImageField(upload_to='avatars',default='no_image.jpg')
    tutoring_experience = models.TextField()
    tutoring_approach = models.TextField()
    language = models.CharField(max_length=50, default='')
    availability = models.CharField(max_length=50, default='')
    subjects = models.ForeignKey(Subjects, blank=False, related_name="subject_tutor", on_delete=models.CASCADE, default='')
    reference = models.CharField(max_length=254, default='')
    
    def __str__(self):
        return self.name