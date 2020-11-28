from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import RequestForm , CreateUserForm
from .decorators import unauthenticated_user, allowed_users , andmin_only

# Create your views here.

#views của homepage
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request,'requestit/index.html', context)

#create request
@login_required(login_url='login')
def create_request(request):
    form = RequestForm()
    context = {'form':form}
    return render(request,'requestit/create_request.html', context)


#tạo view đăng ký
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='nhanvien')
            user.groups.add(group) #tự thêm group vào user
            #gắn user vào tên khách hàng
            Nhanvien.objects.create(user=user,name=user.username,)
            messages.success(request,'Accout was create for '+ username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'requestit/register.html', context)

#tạo view login
@unauthenticated_user
def loginPage(request):
    #nếu chưa đăng nhập thì mới có đến login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Tài khoản hoặc mật khẩu không đúng')
    context = {}
    return render(request,'requestit/login.html', context)

#tạo phần logout
def logoutUser(request):
    logout(request)
    return redirect('login')