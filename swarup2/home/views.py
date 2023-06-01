from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import*
from. forms import*
from home.client import *
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
  


# def toggle_image(request, pk):
#     myimage = get_object_or_404(Image, pk=pk)
#     myimage.is_active = not myimage.is_active
#     myimage.save()
#     data = {'is_active': myimage.is_active}
#     return JsonResponse(data)


def index(request):
    return render(request,'admin_temp/dashboard.html')

#############################################----Login & Logout-----#######################################################
###########################################################################################################################

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully...')

            return redirect('homeT')
        else:
           messages.error(request,'username or password not correct')
           return redirect('login')

          
    return render(request,'client_temp/Login.html')
  
  
def LogoutPage(request):
    logout(request)
    return redirect('login_view')
  
##############################################-------INSERT DATA-------################################################################################################
##############################################################################################################################################
def homeT(request):
    result= manage.objects.all()
    demo=Image.objects.all()
    demos= manage.objects.all()
    slide_data=slider.objects.all()
    return render(request,'homeT.html',{'result':result,'demo':demo,'demos':demos,'slide_data':slide_data})


def AbouT(request):
    result3= AboutT.objects.all()
    demo=aboutI.objects.all()
    return render(request,'admin_temp/aboutT.html',{'result3':result3,'demo':demo})

def AboutI(request):
    result1= aboutI.objects.all()
    return render (request,'admin_temp/aboutI.html',{'result1':result1})
  
def chickT(request):
    result4= chick.objects.all()
    demo= chickI.objects.all()
    return render(request,'admin_temp/chickT.html',{'result4':result4,'demo':demo})
  

def contactT(request):
    result7= contact.objects.all()
    results4=contactI.objects.all()
    demo=contact.objects.all()
    
    # result= contact.objects.all()
    return render(request,'admin_temp/contactT.html',{'result7':result7,'results4': results4,'demo':demo})


def producT(request):
    result2= product.objects.all()
    demo= productI.objects.all()
    return render(request,'admin_temp/producT.html',{'result2':result2,'demo':demo})
  

def peanuT(request):
    result3= peanut.objects.all()
    demo= peanutI.objects.all()
    data= peanut.objects.all()
    return render(request,'admin_temp/peanuT.html',{'result3':result3,'demo':demo,'data':data})
  

def homeI(request):
    results5= slider.objects.all()
    return render (request,'admin_temp/homeI.html',{'results5':results5})
  

def chicksI(request):
    result4= chickI.objects.all()
    result5= chickI.objects.filter(Title='')
    return render (request,'admin_temp/chickI.html',{'result4':result4,'result5':result5})
  

def PeanutI(request):
    result3= peanutI.objects.all()
    result4= peanutI.objects.filter(Title='')
    return render (request,'admin_temp/peanutI.html',{'result3':result3,'result4':result4,})


def ProductI(request):
    result2= productI.objects.all()
    return render (request,'admin_temp/productI.html',{'result2':result2,})


def home(request):
    return render(request,'admin_temp/home.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

# def login(request):
    # return render(request,'login.html')
# def LoginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         User=authenticate(request,username=username,password=password)
#         if User is  None:
#             login(request,User)

#             return redirect('index')
#         else:
#            messages.error(request,'username or password not correct')

#     return render (request,'admin_temp/login.html')

##########################################-----------ADD-----------####################################################################################################
##############################################################################################################################################

def hometextadd(request):
    if request.method =='POST':
    
        Text=request.POST['editor']
        title=request.POST['text']
        print(Text)
        form =manageForm()
        form= manage( text=Text,Title=title)
        form.save()
        messages.success(request, 'Data Added Successfully')
        return redirect('/homeT')
    
# def contacttextadd(request):
#     if request.method =='POST':
    
#         adress=request.POST['editor1']
#         phone=request.POST['phone']
#         email=request.POST['email']
#         # print(Text)
#         form =contactForm()
#         form= contact( Address=adress,Phone=phone,Email=email)
#         form.save()
#         messages.success(request, 'Data Added Successfully')
        
#         return redirect('/contactT')


def contacttextadd(request):
    if request.method =='POST':
    
        adress=request.POST['editor']
        phone=request.POST['phone']
        email=request.POST['email']
        # print(Text)
        # form =contactForm()
        # form= contact( Address=adress,Phone=phone,Email=email)
        # form.save()
        data=f'User Name is {phone},\n User Mail {email}, \n User Comment is {adress}'
        print('5555555555555555555555555')
        
        mailId=settings.EMAIL_HOST_USER
        send_mail('Mail for Swarup',f'Here is your site mail is \n \n {data}',settings.EMAIL_HOST_USER,[mailId])




        messages.success(request, 'Data Added Successfully')
        
        return redirect('/contactT')





















































def chicktextadd(request):
     if request.method =='POST':
    
        Text=request.POST['editor']
        title=request.POST['text']
        print(Text)
        form =chickForm()
        form= chick( text=Text,Title=title)
        form.save()
        messages.success(request, 'Data Added Successfully')

        return redirect('/chickT')
    
def abouttextadd(request):
     if request.method =='POST':
    
        Text=request.POST['editor']
        title=request.POST['text']
        print(Text)
        form =AboutTForm()
        form= AboutT( text=Text,Title=title)
        form.save()
        messages.success(request, 'Data Added Successfully')
        
        return redirect('/AboutT')
    
def producttextadd(request):
     if request.method =='POST':
    
        Text=request.POST['editor']
        title=request.POST['text']
        print(Text)
        form =productTForm()
        form= product( text=Text,Title=title)
        form.save()
        messages.success(request, 'Data Added Successfully')
        
        return redirect('/producT')
    
def peanuttextadd(request):
   if request.method =='POST':
    
        Text=request.POST['editor']
        title=request.POST['text']
        print(Text)
        form =peanutForm()
        form= peanut( text=Text,Title=title)
        form.save()
        messages.success(request, 'Data Added Successfully')
        
        return redirect('/peanuT')

def aboutImgadd(request):
    if request.method =='POST':
        myFiles=request.FILES['myFile']
        Text= request.POST['text']
        form= aboutI( Title=Text,image=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
    return redirect('/AboutT')

def contactImgadd(request):
    if request.method =='POST':
        myFiles=request.FILES['myFile']
        Text= request.POST['text']
        form= contactI( Title=Text,image=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
    return redirect('/contactT')


def peanutImgadd(request):

  if request.method =='POST':
        Text= request.POST['text']
        myFiles=request.FILES['myFile']
        form= peanutI( Title=Text,image=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
        return redirect('/peanuT')

def chickImgadd(request):

   if request.method =='POST':
        myFiles=request.FILES['myFile']
        Text= request.POST['text']
        form= chickI( Title=Text,image=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
        return redirect('/chickT')
    
def HomeImgadd(request):

   if request.method =='POST':
        myFiles=request.FILES['myFile']
        Text= request.POST['text']
        form= slider( Title=Text,image=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
        return redirect('/homeI')

def homeImgadd(request):

    if request.method =='POST':
        myFiles=request.FILES['myFile']
        Text= request.POST['text']
        form= Image( Title=Text,images=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
    return redirect('/homeT')

def productImgadd(request):

    if request.method =='POST':
        Text= request.POST['text']
    
        myFiles=request.FILES['myFile']
    
        form= productI( Title=Text,image=myFiles)
        form.save()
        messages.success(request, 'Image Added Successfully')
        
    return redirect('/producT')

##############################################-------DELETE------################################################################################################
##############################################################################################################################################
 
    
def hometextdel(request, id):
  member = manage.objects.get(id=id)
  member.delete()
  return redirect('/homeT')

def chicktextdel(request, id):
  member = chick.objects.get(id=id)
  member.delete()
  return redirect('/chickT')

def contacttextdel(request, id):
  member = contact.objects.get(id=id)
  member.delete()
  return redirect('/contactT')

def producttextdel(request, id):
  member = product.objects.get(id=id)
  member.delete()
  return redirect('/producT')

def abouttextdel(request, id):
  member = AboutT.objects.get(id=id)
  member.delete()
  return redirect('/AboutT')

def peanuttextdel(request, id):
  member = peanut.objects.get(id=id)
  member.delete()
  return redirect('/peanuT')

def homeImgdel(request, id):
  member = Image.objects.get(id=id)
  member.delete()
  return redirect('/homeT')

def HomeImgdel(request, id):
  member = slider.objects.get(id=id)
  member.delete()
  return redirect('/homeI')

def peanutImgdel(request, id):
  member = peanutI.objects.get(id=id)
  member.delete()
  return redirect('/peanuT')

def contactImgdel(request, id):
  member = contactI.objects.get(id=id)
  member.delete()
  return redirect('/contactT')


def aboutImgdel(request, id):
  member = aboutI.objects.get(id=id)
  member.delete()
  return redirect('/AboutT')

def chickImgdel(request, id):
  member = chickI.objects.get(id=id)
  member.delete()
  return redirect('/chickT')

def prodctuImgdel(request, id):
  member = productI.objects.get(id=id)
  member.delete()
  return redirect('/producT')

#################################################--------UPDATE--------#############################################################################################
##############################################################################################################################################


def homeupdate(request,id):
    if request.method == 'POST':
        Text= request.POST.get('text')
        editor= request.POST.get('editor1')
        
        em= manage(
            id=id,
            text=editor,
            Title= Text
        )
        em.save()
        messages.success(request, 'Data Updated Successfully')
        
        return redirect('/homeT')
    return render(request, 'homeT.html')

def contactupdate(request,id):
    if request.method == 'POST':
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        address= request.POST.get('editor1')
        em= contact(
            id=id,
            Email=email,
            Phone= phone,
            Address= address
        )
        em.save()
        messages.success(request, 'Data Updated Successfully')
        
        print(em)
        return redirect('/contactT')
    # return render(request, 'homeT.html')

def chickupdate(request,id):
    if request.method == 'POST':
        Text= request.POST.get('text')
        editor= request.POST.get('editor1')
        
        em= chick(
            id=id,
            text=editor,
            Title= Text
        )
        em.save()
        messages.success(request, 'Data Updated Successfully')
        
    return redirect("/chickT")


def aboutupdate(request,id):
    if request.method == 'POST':
        Text= request.POST.get('text')
        editor= request.POST.get('editor1')
        
        em= AboutT(
            id=id,
            text=editor,
            Title= Text
        )
        em.save()
        messages.success(request, 'Data Updated Successfully')
        
        return redirect('/AboutT')
    
    return render(request, 'admin_temp/AboutT.html')

def peanutupdate(request,id):
    if request.method == 'POST':
        Text= request.POST.get('text')
        editor= request.POST.get('editor1')
        
        em= peanut(
            id=id,
            text=editor,
            Title= Text
        )
        em.save()
        messages.success(request, 'Data Updated Successfully')
        
        return redirect('/peanuT')
    
    return render(request, 'admin_temp/peanuT.html')



def aboutImgupdate(request,id):
  l=aboutI.objects.get(id=id)
  if request.method=='POST':
    try:
     l.image = request.FILES['myFile']
    except:
     pass
    l.Title= request.POST['text']
    l.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect("/AboutT")
  return render(request,'admin_temp/AboutT.html',{'l':l})


def chickImgupdate(request,id):
 g= chickI.objects.get(id=id)
 if request.method=='POST':
    try:
       g.image = request.FILES['myFile']
    except:
       pass
    g.Title= request.POST['text']
    g.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect("/chickT")
 return render(request,'admin_temp/chickT.html',{'g':g})


def peanutImgupdate(request,id):
  d=peanutI.objects.get(id=id)
  if request.method=='POST':
    try:
      d.image = request.FILES['myFile']
    except:
      pass
    d.Title= request.POST['text']
    
    d.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect("/peanuT")
  return render(request,'admin_temp/peanuT.html',{'d':d})

  
def homeImgupdate(request,id):
  
  c=Image.objects.get(id=id)
  if request.method=='POST':
    c.Title= request.POST['text']
    try:
        c.images = request.FILES['myFile']
    except:
        pass
    c.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect("/homeT")
  return render(request,'admin_temp/homeT.html',{'c':c})

def productImgupdate(request,id):
  i=productI.objects.get(id=id)
  if request.method=='POST':
    try:
       i.image = request.FILES['myFile']
    except:
        pass
    i.Title= request.POST['text']
    
    i.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect("/producT")
  return render(request,'admin_temp/producT.html',{'i':i})


def productupdate(request,id):
     if request.method == 'POST':
        Text= request.POST.get('text')
        editor= request.POST.get('editor1')
        
        em= product(
            id=id,
            text=editor,
            Title= Text
        )
        em.save()
        messages.success(request, 'Data Updated Successfully')
        
        return redirect('/producT')


def contactImgupdate(request,id): 
 c=contactI.objects.get(id=id)
 if request.method=='POST':
    try:
     c.image = request.FILES['myFile']
    except:
      pass
    c.Title= request.POST['text']
    
    c.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect("/contactT")
 return render(request,'admin_temp/contactT.html',{'c':c})

def Sliders(request,id):
  w=slider.objects.get(id=id)
  if request.method=='POST':
    try:
      w.image = request.FILES['myFile']
    except:  
      pass
    w.Title= request.POST['text']
    
    w.save()
    messages.success(request, 'Image Updated Successfully')
    
    return redirect('/homeI')
  return render(request,'admin_temp/homeI.html',{'w':w})
