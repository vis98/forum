from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm
from members.models import user
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import user
from django.http import HttpResponseRedirect, HttpResponse
def register(request):

    if request.method == 'POST':
        f = UserForm(request.POST)
        
        if f.is_valid():
            passw=request.POST['password']
            name=request.POST['username']
            print(passw)
            
            if user.objects.filter(username=name).exists():
                messages.error(request,"already exists")
                
            else: 
                if len(passw)<8:
                    messages.error(request,'password should be greater than 8')
                else:
                    f1=user.objects.create(username=name,password=passw)
                    f1.save()
                    return HttpResponseRedirect(reverse('members:mlogin'))
 
    else:
        f = UserForm()
 
    return render(request, 'register.html', {'form': f})


def Login(request):
    f=None
    if request.method == 'POST':
        f = UserForm(request.POST)
        
        if f.is_valid():
            passw=request.POST['password']
            name=request.POST['username']
            u=user.objects.get(username=name,password=passw)
            if u is not None:
                return HttpResponseRedirect(reverse('posts:list'))
            else:
                messages.error(request,'invalid credentials')
                return redirect('posts:list')    
    else:
        f=UserForm()               

    return render(request, 'login.html', {'form': f})

def Home(request):
    return render(request,'home.html')

   