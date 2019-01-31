from django.shortcuts import render, HttpResponse, get_object_or_404 
from .models import Tutor

# Create your views here.

def get_subject_tutor(request):
    tutor = Tutor.objects.all()
    return render(request, "tutors/subject_tutors.html", {"tutor":tutor})
