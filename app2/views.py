from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':70,'b':80,'c':100}
    return render(request,'a2_first.html',d)