from django.shortcuts import render, HttpResponse, get_object_or_404 
from .models import Subjects

# Create your views here.

def get_subjects(request):
    subjects = Subjects.objects.all()
    return render(request, "subjects/subjects.html", {"subjects":subjects})
