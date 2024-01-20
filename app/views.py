from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            mufdo=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            mufdo.set_password(pw)
            mufdo.save()
            mpfdo=pfd.save(commit=False)
            mpfdo.username=mufdo
            mpfdo.save()
            return HttpResponse('registration is successfull ')

        else:
            return HttpResponse('invalid data')
    return render(request,'registration.html',d)