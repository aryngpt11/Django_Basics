from django.shortcuts import render

# Create your views here.
def dj(request):
    return render (request,'dj.html',context={'dj':'Django'})

def py(request):
    return render (request,'py.html',context={'py':'Python'})