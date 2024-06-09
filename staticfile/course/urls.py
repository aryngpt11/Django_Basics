from course.views import *
from django.urls import path

urlpatterns = [
    path('dj/',dj,name='dj'),
    path('py/',py,name='py'),
]
