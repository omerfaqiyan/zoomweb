from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from mysite.core import codes
from mysite.core import reformatfunctions
from mysite.core import temp
def index(request):
    context = {}
    return render(request, 'upload.html', context)

def upload(request):
    context = {}
    if request.method == 'POST':
        if request.FILES == {}:
         return redirect('/')
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        outputname=name[:-4]+"-output.csv"
        a=temp.reformzoom(name)
        if a==1:
            context['url']=fs.url(outputname)
        else:
            context['url']=fs.url("errormsg.csv")


       
    return render(request, 'upload.html', context)






