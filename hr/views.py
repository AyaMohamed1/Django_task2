from multiprocessing import context
from django.shortcuts import render
from .models import Myuser
from django.shortcuts import redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login as authLogin, logout as authLogout
from student_register.views import student_list
# Create your views here.

# @csrf_protect 
def hrhome(request):
    return render(request,'hr/home.html')


def mylogout(request):
    authLogout(request)
    return render(request,'hr/home.html')

def register(request):
    # browser default
    if(request.method == 'GET'):    
        return render(request, 'hr/register.html')
    # pressed register so it's POST
    # put data in database model then render to login
    else:
        Myuser.objects.create(username=request.POST['username'],password=request.POST['password'])
        User.objects.create_user(username=request.POST['username'],password=request.POST['password'], is_staff=True)
        # return render(request, 'hr/login.html')
        return redirect(login)

def login(request):
    if(request.method == 'GET'):
        return render(request, 'hr/login.html')
    else:
        # Check pass and username
        user = Myuser.objects.filter(username=request.POST['username'], password=request.POST['password'])
        authUser = authenticate(username=request.POST['username'], password=request.POST['password'])
        # render home
        if len(user) > 0 and authUser is not None:
            context = {}
            request.session['username'] = request.POST['username']
            authLogin(request, authUser)
            return redirect('student_list')
            # context['username'] = user[0].username
            # return HttpResponseRedirect('hr', context)
            
        else:
            context = {}
            context['msg'] = 'invalid username or password!'
            return render(request, 'hr/login.html', context)
            
    

# def checklogin(request):
#     if request.method == 'POST':
#         # Check pass and username
#         user = Myuser.objects.filter(username=request.POST['username'], password=request.POST['password'])
#         # render home
#         if user is not None:
#             return redirect(hrhome)
#         else:
#             return redirect(login, {'msg': 'invalid user'})
        
