from django.shortcuts import render
from django.http import  HttpResponseRedirect
from  .forms import Signup,Student
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login , logout
from .models import Studentinfo,Studentmark
# Create your views here.

#home
def home(request):
    stu =  Studentmark.objects.all()
    return render(request,'home.htm',{'stu':stu})

#signup
def signup(request):
    if request.method == 'POST':
        sf = Signup(request.POST)
        if sf.is_valid():
            sf.save()
            sf = Signup()
            messages.success(request,'SIGNUP SUCCESSFUL !!!!')
    else:
        sf = Signup()    
        
    return render (request,'signup.htm',{'sf':sf})

#login
def login(request):
    if request.method == 'POST':
        lf = AuthenticationForm(request ,data=request.POST)
        if lf.is_valid():
            uname = lf.cleaned_data['username']
            upass = lf.cleaned_data["password"]
            user = authenticate(username = uname,password = upass)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/dashboard/')
                   
    else:
        lf = AuthenticationForm(request ,data=request.POST)
             
    return render(request,'login.htm',{'lf':lf})

#logout
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        stu = Studentinfo.objects.all()
        name = request.user
    else:
        return HttpResponseRedirect('/login/') 
              
    return render(request,'dashboard.htm',{'stu':stu,'name':name})

#edit
def edit(request,id):
    if request.method == 'POST':
        info = Studentinfo.objects.get(pk = id)
        stu = Student(request.POST,instance=info)
        if stu.is_valid():
            stu.save()
            return  HttpResponseRedirect('/dashboard/')
    else:
        info = Studentinfo.objects.get(pk = id)
        stu = Student(instance=info)
    return render(request,'edit.htm',{'stu':stu})


#delete
def delete(request,id):
    if request.user.is_authenticated:
            info = Studentinfo.objects.get(pk=id)
            info.delete()
            return  HttpResponseRedirect('/dashboard/')
    else:
        return  HttpResponseRedirect('/delete/')       


#add
def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ns = Student(request.POST)
            if ns.is_valid():
                ns.save()
                HttpResponseRedirect('/dashboard/')    

        else:
            ns = Student()        
        return render(request,'add.htm',{'ns':ns})                
    else:
        HttpResponseRedirect('/login/')    


#about 
def about(request):
    return render(request,'about.htm')