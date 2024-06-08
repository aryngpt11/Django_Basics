from django.urls import path
from fees.views import *
urlpatterns = [
    path('fee_django/',fee_django,name='fee_django'),
    path('fee_python/',fee_python,name='fee_python')
]