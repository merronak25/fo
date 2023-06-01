from django import forms
from .models import *
from ckeditor_uploader.widgets import  CKEditorUploadingWidget

class manageForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model= manage
        fields= '__all__'
        
class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= '__all__'
        
class aboutIForm(forms.ModelForm):
    # image = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model= aboutI
        fields= '__all__'

class AboutTForm(forms.ModelForm):
    # text = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model= AboutT
        fields= '__all__'
        
class productTForm(forms.ModelForm):
    # text = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model= product
        fields= '__all__'
        
class peanutForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model= peanut
        fields= '__all__'
    
class chickForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model= chick
        fields= '__all__'
    
class contactIForm(forms.ModelForm):
    class Meta:
        model= contactI
        fields= '__all__'
        
class contactForm(forms.ModelForm):
    class Meta:
        model= contact
        fields= '__all__'