from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fee_django(request):
    return render(request,'feesone.html',context={'fe':'FeeDjango'})

def fee_python(request):
    return HttpResponse("<h1> 20000</h1>")