from django.shortcuts import render
from studinfo.models import Student
# Create your views here.
def studentinfo(request):
    stu=Student.objects.all()
    #stu=Student.objects.get(pk=2)
    return render(request, 'studinfo/studetails.html', {'stu':stu})