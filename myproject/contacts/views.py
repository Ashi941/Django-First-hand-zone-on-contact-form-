from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel
# Create your views here.

#First argument always be the request
def home_page(request):
    #Return an HTTP Response
    # return HttpResponse("Welcome !")
    #Return a html response -HttpRespone("text")
    #Return HTML Response - render(request,"html file",context)
    return render(request,"home.html")


def contact_us(request):
    #Insert post data to table
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")
        obj = MyModel.objects.create(name=name,email=email,mobile=mobile,message=message)
        print("Succesfully created")
        #Show homw page after submission
        return render(request,"home.html")
    return render(request,"contact.html")