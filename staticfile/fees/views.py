from django.shortcuts import render

# Create your views here.
def djj(request):
    return render (request,'djf.html',context={'djj':'DjangoFee'})

def pyy(request):
    return render (request,'pjf.html',context={'pyy':'PythonFee'})