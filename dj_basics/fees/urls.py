from django.urls import path
from fees.views import *
urlpatterns = [
    path('fees_django/',fees_django,name='fees_django'),
    path('fees_Python/',fees_Python,name='fees_Python'),

   

]