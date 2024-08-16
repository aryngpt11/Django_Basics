from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm=StudentRegistration(auto_id=True , label_suffix=' ', initial={ 'name':'Aryan'})
    return render(request,'userregistration.html',{'form':fm}) 