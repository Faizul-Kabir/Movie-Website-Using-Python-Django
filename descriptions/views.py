from django.shortcuts import render,redirect
from .models import Description
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def descriptions_list(request):
    descriptions=Description.objects.all().order_by('date')
    return render(request,'descriptions/descriptions_list.html',{'descriptions':descriptions})

def details(request,title):
    description=Description.objects.get(title=title)
    return render(request,'descriptions/movie_details.html',{'description':description})

@login_required(login_url="/account/login")
def addmovie_form(request):
    if request.method=='POST':
        form=forms.AddMovie(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('descriptions:list')


    else:

        form=forms.AddMovie()
    return render(request,'descriptions/addmovie.html',{'form':form})



    
