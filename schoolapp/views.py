from django.contrib.messages import constants as messages
from django.contrib import auth, messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department,Courses,Student
from.forms import StudentForm



# Create your views here.


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login Success")
            return redirect('student_add')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login')
    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password!=cpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/register')

        try:
            if User.objects.get(username=username):
                messages.info(request,"UserName Is Taken")
                return redirect('/register')
        except:
            pass
        
        user=User.objects.create_user(username,password)
        user.save()
        messages.success(request,"Signup Success Please login!")
        return redirect('/login')
    return render(request,'register.html')
        
def logout(request):
    auth.logout(request)
    messages.success(request,"Logout Success")
    return redirect('/')
    
def student_create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Form saved !")
            return redirect('/confirm')
    return render(request, 'requirements.html', {'form': form})


def student_update_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_change', pk=pk)
    return render(request, 'requirements.html', {'form': form})

def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id=department_id).all()
    return render(request,'courses_dropdown.html', {'courses':courses})
    
def confirm(request):
    return render(request,'confirm.html')