from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import*
from. forms import*


def clientIndex(request):
    slide_data= slider.objects.all()
    demos= manage.objects.all()
    result3= Image.objects.all()
    results=Image.objects.all()
    
    for i in range(len(slide_data)):
        if i==0:
            slide_data[i].activate = True
        else:
            slide_data[i].activate = False
    return render(request, 'client_temp/index.html', {'slide_data': slide_data, 'result3': result3,'demos':demos,'results': results,})

    # return render(request,'client_temp/index.html')

def client_peanut(request):
    data= peanut.objects.all()
    results=peanutI.objects.all()
    return render(request,'client_temp/peanut.html',{'data':data,'results':results})

def client_chick(request):
    results=chickI.objects.all()
    result=chick.objects.all()
    return render(request,'client_temp/Chickpeas.html',{'results':results,'result':result})

def client_product(request):
    demo=productI.objects.all()
    sub=product.objects.all()
    return render(request,'client_temp/product.html',{'demo':demo,'sub':sub})

def client_about(request):
    demo=aboutI.objects.all()
    para=AboutT.objects.all()
    return render(request,'client_temp/about.html',{'demo':demo,'para':para})

def client_contact(request):
    demo=contactI.objects.all()
    result7=contact.objects.all()
    return render(request,'client_temp/contact-us.html',{'demo':demo,'result7':result7})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
        
    return render(request,'client_temp/login.html')