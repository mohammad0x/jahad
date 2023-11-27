from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.http import HttpResponse
from login.views import is_active_on_panel
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from login.forms import *
from .forms import *
from login.forms import *
from login.models import *


def Logout_view(request):
    logout(request)
    return redirect('login:login')





@login_required(login_url='/login/')
@is_active_on_panel
def GroupUpdate(request):
    if request.method == 'POST':
        user_form = UserUpForm(request.POST, instance=request.user)
        group_form = GroupCreateForm(request.POST, request.FILES, instance=request.user.Group)
        if user_form.is_valid() or group_form.is_valid():
            user_form.save()
            group_form.save()
            messages.success(request, 'اطلاعات گروه جهادی با موفقیت ویرایش شد', 'success')
            return redirect('panel:panel')

    else:
        user_form = UserUpForm(instance=request.user)
        group_form = GroupCreateForm(instance=request.user)
        admin = MyUser.objects.get(id=request.user.id)
        group = MyUser.objects.get(id=request.user.id)
        admin_panel = Group.objects.get(id=request.user.id)
        group_panel = Group.objects.get(id=request.user.id)


    context = {'user_form': user_form, 'group_form': group_form,
               'admin_name': admin.admin_name,
               'admin_last':admin.admin_lastname,
               'group_name': group.group_name,
               'nati':admin.nationality_code,
               'gharargah':group_panel.gharargah

               }
    return render(request, 'group_j/panel.html', context)



@login_required(login_url='/login/')
@is_active_on_panel
def AdminUpdate(request):
    if request.method == 'POST':
        user_form = UserUpForm(request.POST, instance=request.user)
        group_form = UserUpFormM(request.POST, instance=request.user.Group)

        if user_form.is_valid() or group_form.is_valid:
            user_form.save()
            group_form.save()
            messages.success(request, 'اطلاعات ادمین گروه جهادی با موفقیت ویرایش شد', 'success')
            return redirect('panel:panel')

    else:
        user_form = UserUpFormM(instance=request.user)
        group_form = UserUpForm(instance=request.user)
        admin = MyUser.objects.get(id=request.user.id)
        adminn = Group.objects.get(id=request.user.id)
    context = {'user_form': user_form ,
               'group_form': group_form,
               'name':admin.admin_name,
               'last':admin.admin_lastname,
               'ph':adminn.phone,
               'date':adminn.date,
               'nation':admin.nationality_code

               }
    return render(request, 'admin/panel.html', context)




@login_required(login_url='/login/')
@is_active_on_panel
def ArkanUpdate(request):
    if request.method== 'POST':
        user = request.user.id
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        semat = request.POST.get('semat')
        phone = request.POST.get('phone')
        Arkan.objects.create(user_id = user , name=name ,
                             last_name=last_name , semat=semat , phone=phone)

        messages.success(request, 'رکن شما با موفقیت ساخته شد', 'success')

        return redirect('panel:panel')
        return render(request,'arkan/panel.html')

    else:
        return render(request,'arkan/panel.html')

@login_required(login_url='/login/')
@is_active_on_panel
def ActivetyUpdate(request):
    if request.method == 'POST':
        activity_form = ActivetyUpdateForm(request.POST, instance=request.user.Activety)
        if activity_form.is_valid():
            activity_form.save()
            messages.success(request, 'اطلاعات فعالیت های گروه جهادی با موفقیت ویرایش شد', 'success')
            return redirect('panel:panel')
    else:
        activity_form = ActivetyUpdateForm(instance=request.user)
        acc = Activety.objects.get(id=request.user.id)
    context = {'activity_form': activity_form,
               'arsefa': acc.arsefa,
               'tedadshe':acc.tedadshe,
               'date':acc.date,
               'numberhokm':acc.numberhokm,
               'name_masol':acc.name_masol,
               'phone_masol':acc.phone_masol,
               'message':acc.message
               }
    return render(request, 'faalivat/panel.html', context)


@login_required(login_url='/login/')
@is_active_on_panel

def Panel(request):
    myuser = MyUser.objects.get(id=request.user.id)
    mygroup = Group.objects.get(user_id=request.user.id)
    g = get_object_or_404(Group , user_id=request.user.id)
    # print(g.gharargah.gharargah_name )

    context = {
        'adminFirst': myuser.admin_name,
        'adminLast': myuser.admin_lastname,
        'group_n': myuser.group_name,
        'nation': myuser.nationality_code,
        'adress':mygroup.adress,
        'num':mygroup.number_sa,
        'g':g

    }

    return render(request, 'panel/panel.html', context)


@login_required(login_url='/login/')
@is_active_on_panel

def Contact_To_admin(request):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        mozo = request.POST['mozo']
        image = request.POST['image']



        Contact_to_admin.objects.create(name=name, message=message , mozo=mozo , image=image)
        messages.success(request, 'گزارش شما با موفقیت ارسال شد ', 'success')
        return redirect('panel:panel')

    arkan = Arkan.objects.filter(user_id=request.user.id)
    activety = Activety.objects.filter(user_id=request.user.id)

    context = {
        'arkan': arkan,
        'activety': activety
     }
    return render(request, 'gozaresh/gozaresh.html' ,context)




@login_required(login_url='/login/')
def Payam(request):
    post = Contact_to_user.objects.filter(status='p',view_id=request.user.id)
    context = {'post': post}
    return render(request, 'gozaresh/post.html', context)


@login_required(login_url='/login')

def dastrasi(request):
    return render(request, 'panel/dastrasi.html')

def home(request):
    return render(request,'home/home_before_login.html')






@login_required(login_url='/login/')
@is_active_on_panel
def GroupUpdateTow(request):
    if request.method == 'POST':
        group_form = GroupCreateForml(request.POST, request.FILES, instance=request.user.Group)
        if  group_form.is_valid():
            group_form.save()
            messages.success(request, 'اطلاعات گروه جهادی با موفقیت ویرایش شد', 'success')
            return redirect('panel:panel')

    else:
        group_form = GroupCreateForm(instance=request.user)
        group = MyUser.objects.get(id=request.user.id)
        group_panel = Group.objects.get(id=request.user.id)


    context = {'group_form': group_form,
               'group_name': group.group_name,
               'gharargah':group_panel.gharargah
               }
    return render(request, 'group_j/panel_group_f_panel.html', context)
