from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied

from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from panel.forms import *


# Create your views here.




def Register(request):
    if request.user.is_authenticated:
        return redirect('login:login')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        nationality_code = form['nationality_code'].value()
        group_name = form['group_name'].value()
        if MyUser.objects.filter(nationality_code=nationality_code).exists():
            messages.error(request, 'کد ملی مسئول گروه جهادی شما تکراری است.', 'danger')
            return redirect('login:register')
        if MyUser.objects.filter(group_name=group_name).exists():
            messages.error(request, 'نام گروه جهادی شما تکراری است', 'danger')
            return redirect('login:register')
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(nationality_code=data['nationality_code'], password=data['password'] , group_name=data['group_name'] , admin_name=data['admin_name'] , admin_lastname= data['admin_lastname'])
            # user.save()
            login(request, user)
            messages.success(request, 'گروه جهادی شما با موفقیت ساخته شد به پنل کاربری منتقل می شوید', 'success')
            return redirect('login:login')
        else:
            messages.error(request, 'خظای غیر منتظره رخ داده است', 'danger')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'register/register.html')


def Login(request):
    if request.user.is_authenticated:
        group = Group.objects.filter(user_id=request.user.id)
        for groups in group:
            if groups.adress is not None:
                return redirect('panel:panel')
            else:
                return redirect('panel:groupupdate')

    if request.method == 'POST':
        nationality_code = request.POST.get('nationality_code')
        password = request.POST.get('password')
        user = authenticate(request, nationality_code=nationality_code, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'ورود با موفقیت انجام شد', 'success')

            group = Group.objects.filter(user_id=request.user.id)
            for groups in group:
                if groups.adress is not None:
                    return redirect('panel:panel')
                else:
                    return redirect('panel:groupupdate')

        else:
            context = {
                "nationality_code": nationality_code,
                "errormessage": "User not found"
            }
            return render(request, "login/login.html", context)
    else:
        return render(request, 'login/login.html', {})

@login_required(login_url='/login/')
def Logout_view(request):
    logout(request)
    return redirect('login:login')


def is_active_on_panel(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_active_on_panel:
            return redirect("panel:dastrasi")
            raise PermissionDenied
        return func(request,*args,**kwargs)
    return wrapper



