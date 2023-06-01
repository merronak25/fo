from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


from home.client import *



urlpatterns = [
    path('index/',views.index,name='index'),
    path('homeI/',views.homeI,name='homeI'),
    path('PeanutI/',views.PeanutI,name='PeanutI'),
    path('chicksI/',views.chicksI,name='chicksI'),
    path('chickImgadd/',views.chickImgadd,name='chickImgadd'),
    path('contactImgadd/',views.contactImgadd,name='contactImgadd'),
    
    
    path('AboutI/',views.AboutI,name='AboutI'),
    path('ProductI/',views.ProductI,name='ProductI'),
    
    path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
    path('login/', views.login_view, name='login'),
    # path('homes/', views.homeS, name='login'),
    path('homeT/', views.homeT, name='homeT'),
    path('chickT/', views.chickT, name='chickT'),
    path('contactT/', views.contactT, name='contactT'),
    
    
    path('peanuT/', views.peanuT, name='peanuT'),
    
    path('AboutT/', views.AbouT, name='AbouT'),
    path('producT/', views.producT, name='producT'),
    # path('productT/', views.productT, name='productT'),
    
    path('peanuttextadd/', views.peanuttextadd, name='peanuttextadd'),
    path('contacttextadd/', views.contacttextadd, name='contacttextadd'),
    
    path('hometextadd/', views.hometextadd, name='hometextadd'),
    path('aboutImgadd/', views.aboutImgadd, name='aboutImgadd'),
    path('productImgadd/', views.productImgadd, name='productImgadd'),
    path('peanutImgadd/', views.peanutImgadd, name='peanutImgadd'),
    path('homeImgadd/', views.homeImgadd, name='homeImgadd'),
    path('logout/', views.logout, name='logout'),
    
    path('abouttextadd/', views.abouttextadd, name='abouttextadd'),
    path('chicktextadd/', views.chicktextadd, name='chicktextadd'),
    
    
    path('hometextdel/<int:id>', views.hometextdel, name='hometextdel'),
    path('aboutImgdel/<int:id>', views.aboutImgdel, name='aboutImgdel'),
    
    path('chicktextdel/<int:id>', views.chicktextdel, name='chicktextdel'),
    path('contacttextdel/<int:id>', views.contacttextdel, name='contacttextdel'),
    
    path('productImgupdate/<int:id>', views.productImgupdate, name='productImgupdate'),
    path('contactImgupdate/<int:id>', views.contactImgupdate, name='contactImgupdate'),
    path('Sliders/<int:id>', views.Sliders, name='sliders'),
    
    path('homeupdate/<int:id>', views.homeupdate, name='homeupdate'),
    path('aboutupdate/<int:id>', views.aboutupdate, name='aboutupdate'),
    path('productupdate/<int:id>', views.productupdate, name='productupdate'),
    path('peanutImgupdate/<int:id>', views.peanutImgupdate, name='peanutImgupdate'),
    path('chickImgupdate/<int:id>', views.chickImgupdate, name='chickImgupdate'),
    
    path('peanutupdate/<int:id>', views.peanutupdate, name='peanutupdate'),
    path('chickupdate/<int:id>', views.chickupdate, name='chickupdate'),
    path('peanutImgdel/<int:id>', views.peanutImgdel, name='peanutImgdel'),
    path('chickImgdel/<int:id>', views.chickImgdel, name='chickImgdel'),
    
    
   
    
    
    
    path('contactupdate/<int:id>', views.contactupdate, name='contactupdate'),
    
    path('HomeImgadd/', views.HomeImgadd, name='HomeImgadd'),
    
    path('producttextadd/', views.producttextadd, name='producttextadd'),
    path('contactImgdel/<int:id>', views.contactImgdel, name='contactImgdel'),
    path('HomeImgdel/<int:id>', views.HomeImgdel, name='HomeImgdel'),
    
    path('homeImgdel/<int:id>', views.homeImgdel, name='homeImgdel'),
    path('producttextdel/<int:id>', views.producttextdel, name='producttextdel'),
    
    
    path('homeImgupdate/<int:id>', views.homeImgupdate, name='homeImgupdate'),
    path('aboutImgupdate/<int:id>', views.aboutImgupdate, name='aboutImgupdate'),
    
    path('abouttextdel/<int:id>', views.abouttextdel, name='abouttextdel'),
    path('productImgdel/<int:id>', views.prodctuImgdel, name='prodctuImgdel'),
    
    path('peanuttextdel/<int:id>', views.peanuttextdel, name='peanuttextdel'),
    
    
    

    
    #####################################################################################3
    path('clientIndex/', clientIndex, name="clientIndex"),
    path('client_peanut/', client_peanut, name="client_peanut"),
    path('client_chick/', client_chick, name="client_chick"),
    path('client_product/', client_product, name="client_product"),
    path('client_about/', client_about, name="client_about"),
    path('client_contact/', client_contact, name="client_contact"),
    
    
    
    
    # path('toggle_image/<int:pk>/', views.toggle_image, name='toggle_image'),
    
    # path('homeT/', views.homeT, name='homeT'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

