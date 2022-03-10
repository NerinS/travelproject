from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Place1
# Create your views here.
# def demo(request):
#     return HttpResponse("I like python")
# def home(request):
#     return render(request,"home.html")
# def contact(request):
#     return HttpResponse( "pls contact me")
# def about(request):
#     return render(request,"about.html")
# def details(request):
#     return HttpResponse( "see the details")
# def thanks(request):
#     return HttpResponse( "Thank you for the task")
def demo(request):
    obj = Place.objects.all()
    obj1 = Place1.objects.all()
    return render(request, "index.html",{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3 })
# def demo(request):
#     name = "India"
#     return render(request, "index1.html", {'obj': name})