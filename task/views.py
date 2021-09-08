
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from .models import UserModel
from .forms import UserForm

def indexPage(request):
    return render(request,"indexpage.html")

def signupHere(request):
    user_form=UserForm()
    return render(request,"signup_page.html",{'userform':user_form})

def signupPage(request):
    name=request.POST['user_name']
    email=request.POST['user_email_id']
    pwd=request.POST['password']
    password=make_password(pwd)
    UserModel(user_name=name,user_email_id=email,password=password).save()
    qs=UserModel.objects.all()
    return render(request,"indexpage.html",{"data":qs,"msg":"User registration successfully completed"})

def loginPage(request):
    uf=UserForm()
    return render(request,"login.html",{'form':uf})

def signinPage(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
          user=UserModel.objects.get(user_email_id=email)
          if user:
              uname=user.user_name
              flag=check_password(password,user.password)
              print(flag)
              if flag:
                  return render(request,'welcome.html',{'name':uname})
              else:
                  return render(request,"login.html",{'msg':'Invalid email or password please login again'})
          else:
              return render(request,"login.html",{'msg':'email or password invalid'})
        except:
            return False
















