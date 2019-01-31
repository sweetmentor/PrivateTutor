from django.conf.urls import url
from tutors.views import get_subject_tutor

urlpatterns = [
    url(r'^$', get_subject_tutor, name='subjects_tutor')
    ]