from django.utils import timezone
from django.db import models
from login.models import MyUser
from django.db.models.signals import post_save

# Create your models here.
class Arkan(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name = "رکن گروه جهادی ظ‍به کد ملی .. است", related_name='arkan')
    name = models.CharField(max_length=80,verbose_name='نام')
    last_name = models.CharField(max_length=80,verbose_name='نام خانوادگی')
    semat = models.CharField(max_length=11,verbose_name='سمت')
    phone = models.CharField(max_length=11,verbose_name='شماره تماس')


    def __str__(self):
        return self.user.group_name
def save_arkan_user(sender, **kwargs):
    if kwargs['created']:
        Arkan_user = Arkan(user=kwargs['instance'])
        Arkan_user.save()


post_save.connect(save_arkan_user, sender=MyUser)

class Activety(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='Activety',verbose_name='گروه جهادی')
    arsefa = models.CharField(max_length=80,verbose_name='عرصه فعالیت')
    tedadshe = models.CharField(max_length=80,verbose_name='تعداد شرکت کنندگان')
    date = models.CharField(null=True,max_length=80,verbose_name='تاریخ')
    numberhokm = models.CharField(max_length=20,verbose_name='شماره حکم')
    name_masol = models.CharField(max_length=30,verbose_name='نام و نام خانوادگی مسئول اردو')
    phone_masol = models.CharField(max_length=11,verbose_name='شماره تلفن مسئول گروه')
    message = models.CharField(max_length=500,verbose_name='شرح فعالیت')

    def __str__(self):
        return self.user.group_name


def save_Activety_user(sender, **kwargs):
    if kwargs['created']:
        Activety_user = Activety(user=kwargs['instance'])
        Activety_user.save()

post_save.connect(save_Activety_user, sender=MyUser)


class Contact_to_admin(models.Model):

    name = models.CharField(max_length=40 , verbose_name = "نام ارسال کننده پیغام")
    mozo = models.CharField(max_length=40 , verbose_name = "موضوع")
    image = models.ImageField(upload_to='image',verbose_name='عکس')
    message = models.TextField(verbose_name='پیغام')
    publish = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')



    def __str__(self):
        return self.mozo

class Contact_to_user(models.Model):
    STATUS_CHOICES = (
        ('p', 'ارسال شود'),
        ('d', 'ذخیره شود بعدا ارسال می کنم')
    )
    view = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name = "...ارسال شود به ", related_name='view')
    name = models.CharField(max_length=40 , verbose_name = "نام و نام خانوادگی ارسال کننده پیام")
    mozo = models.CharField(max_length=80 , verbose_name = "موضوع")
    image = models.ImageField(upload_to='image/',verbose_name='عکس')
    message = models.TextField(verbose_name='پیغام')
    publish = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار این پیام')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES , verbose_name="نوع وضغیت را انتخاب کنید")



    def __str__(self):
        return self.view.group_name


