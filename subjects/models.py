from django.db import models
# from tutors.models import Tutor

# Create your models here.
class Subjects(models.Model):
    name = models.CharField(max_length=254, default='') 
    # tutor = models.ForeignKey(Tutor, blank=False, related_name="subjects_tutor", on_delete=models.CASCADE)



    
    def __str__(self):
        return self.name