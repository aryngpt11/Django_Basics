from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm=StudentRegistration()
    return render(request,'userregistration.html',{'form':fm}) 