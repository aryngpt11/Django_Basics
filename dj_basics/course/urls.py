from django.urls import path
from course.views import *
urlpatterns = [
    path('learn_django/',learn_django,name='learn_django'),
    path('learn_Python/',learn_Python,name='learn_Python'),

   

]