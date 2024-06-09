from fees.views import *
from django.urls import path

urlpatterns = [
    path('djj/',djj,name='djj'),
    path('pyy/',pyy,name='pyy'),
]
