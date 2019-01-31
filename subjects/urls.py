from django.conf.urls import url
from subjects.views import get_subjects

urlpatterns = [
    url(r'^$', get_subjects, name='subjects')
    ]