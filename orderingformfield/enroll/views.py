from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm=StudentRegistration()
    fm.order_fields(field_order=['email','name '])
    return render(request,'userregistration.html',{'form':fm}) 