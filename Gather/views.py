from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from django.conf import settings  
from django.conf.urls.static import static  

def Gather(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

urlpatterns = []
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  