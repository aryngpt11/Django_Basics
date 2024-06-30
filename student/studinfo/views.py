from django.shortcuts import render
from studinfo.models import Student
# Create your views here.
def studentinfo(request):
    stu=Student.objects.all()
    return render(request, 'studinfo/studetails.html', {'stu':stu})