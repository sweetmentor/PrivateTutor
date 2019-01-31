from django.shortcuts import render, HttpResponse, get_object_or_404 
from .models import Tutor
# from review.forms import ReviewForm
# from review.models import Review
# Create your views here.

def get_subjects(request):
    
    return render(request, "subjects/subjects.html")
