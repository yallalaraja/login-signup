from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def regView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        # return render(request,'registration/signup.html',{'form':form})
    
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

# login view function to get the login page
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_msg = 'Invalid username or password'
    else:
        error_msg = None
    
    return render(request,'registration/login.html',{'error_msg':error_msg})

def logoutView(request):
    logout(request)
    return redirect('login')