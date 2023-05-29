from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def first(request):
    return HttpResponse("<h1>This is my first web page</h1>")

def login(request):
    if request.method == "POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            data=UserRegister.objects.get(email=email1,password=password1)
            if data:
                request.session['email']=data.email
                print(request.session['email'])
                return redirect('index')
            else:
                return render(request,'login.html',{'message':'Invalid email or password'})
        except:
            return render(request,'login.html',{'message':'Invalid email or password'})
    return render(request,'login.html')

def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('index')
    else:
        return redirect('index')



def table_all(request):
    a=UserRegister.objects.all()
    print("data",a)
    return render(request,'table.html',{"data":a})


def table_filter(request):
    a=UserRegister.objects.filter(email='demo@gmail.com')
    print("data",a)
    return render(request,'table.html',{"data":a})



def table_get(request):
    a=UserRegister.objects.get(email='d@gmail.com')
    print("data",a)
    return render(request,'table_get.html',{"data":a})

def index(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Category.objects.all()
        return render(request,'base.html',{'data':data,'a':a})
    else:
        data=Category.objects.all()
        return render(request,'base.html',{'data':data})

def productall(request):
    if 'email' in request.session:
        a=request.session['email']
    
        data=Product.objects.all()
        return render(request,'productall.html',{'data':data,'a':a})
    else:
        data=Product.objects.all()
        return render(request,'productall.html',{'data':data})
   
        


def productcategorywise(request,id):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.filter(category=id)
        return render(request,'productall.html',{'data':data,'a':a})
    else:
        data=Product.objects.filter(category=id)
        return render(request,'productall.html',{'data':data,'a':a})


def singleproduct(request,id):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.get(pk=id)
        return render(request,'singleproduct.html',{'data':data,'a':a})
    else:
        data=Product.objects.get(pk=id)
        return render(request,'singleproduct.html',{'data':data})

def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['password']
        phone1=request.POST['phone']
        address1=request.POST['address']
        print(name1,email1,password1,address1,phone1)
        data=UserRegister(name=name1,email=email1,password=password1,phone=phone1,address=address1)
        a=UserRegister.objects.filter(email=email1)
        if len(a)==0:
            data.save()
            return redirect('login1')
        else:
            return render(request,'register.html',{'message':"user alredy exist"}) 

    return render(request,'register.html')  

def changepass(request):
   if 'email' in request.session:
        a=request.session['email']
        user=UserRegister.objects.get(email=a)
        if request.method=="POST":
            oldpass=request.POST['oldpass']
            newpass=request.POST['newpass']
            newpass1=request.POST['newpass1']
            if oldpass==user.password:
                if newpass==newpass1:
                    user.password=newpass
                    user.save()
                    return render(request,'changepass.html',{'message':"Password Updated",'a':a})
                    

                else:
                    return render(request,'changepass.html',{'message':"New password not match",'a':a})
            else:
                return render(request,'changepass.html',{'message':"old password not match",'a':a})


           # print(oldpass,newpass,newpass1)

        return render(request,'changepass.html',{'a':a})
   else:
       return redirect('login1')
     

def contactus(request):
    if 'email' in request.session:
        a=request.session['email']
        data=UserRegister.objects.get(email=a)
        if request.method=="POST":
            contact_us=Contactus()
            contact_us.name=request.POST['name']
            contact_us.email=request.POST['email']
            contact_us.msg=request.POST['message']
            contact_us.save()
            return render(request,'contact.html',{'message':"Message Sent",'a':a})
            
        return render(request,'contact.html',{'data':data,'a':a})
    else:
        if request.method=="POST":
            contact_us=Contactus()
            contact_us.name=request.POST['name']
            contact_us.email=request.POST['email']
            contact_us.msg=request.POST['message']
            contact_us.save()
            return render(request,'contact.html',{'message':"Message Sent",'a':a})
           
        return render(request,'contact.html')
