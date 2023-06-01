from django.db import models
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# from djrichtextfield.models import RichTextField

class manage(models.Model):
    text= models.CharField(max_length=10000)
    Title= models.CharField(max_length=100)

class Image(models.Model):
    images = models.FileField(upload_to='img/')
    Title= models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    
class aboutI(models.Model):
    image = models.FileField(upload_to='img/',null=True)
    Title= models.CharField(max_length=100,null=True)

class productI(models.Model):
    image = models.FileField(upload_to='img/')
    Title= models.CharField(max_length=100)
    

class chickI(models.Model):
    image = models.FileField(upload_to='img/')
    Title= models.CharField(max_length=100)
    

class peanutI(models.Model):
    image = models.FileField(upload_to='img/')
    Title= models.CharField(max_length=100)
    
class AboutT(models.Model):
    text= models.CharField(max_length=10000)
    image = models.FileField(upload_to='img/',null= True)
    Title= models.CharField(max_length=100)

    
class product(models.Model):
    text= models.CharField(max_length=10000)
    image = models.FileField(upload_to='img/',null= True)
    Title= models.CharField(max_length=100)

class peanut(models.Model):
    text= models.CharField(max_length=10000)
    image = models.FileField(upload_to='img/',null= True)
    Title= models.CharField(max_length=100)

class chick(models.Model):
    text= models.CharField(max_length=10000)
    image = models.FileField(upload_to='img/',null= True)
    Title= models.CharField(max_length=100)

class contact(models.Model):
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Address = models.TextField(max_length=100)

class slider(models.Model):
    image = models.FileField(upload_to='img/')
    Title= models.CharField(max_length=100)

class contactI(models.Model): 
    image = models.FileField(upload_to='img/')
    Title= models.CharField(max_length=100)


   


    
