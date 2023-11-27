from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.utils import timezone


# Create your models here.

class Garargah(models.Model):
    username = models.CharField(max_length=100, verbose_name='نام کاربری قرار گاه(به انگلیسی وارد شود)')
    gharargah_name = models.CharField(max_length=100, verbose_name='نام قرار گاه')
    admin_name = models.CharField(max_length=100, verbose_name='نام مسئول قرارگاه ')
    admin_lastname = models.CharField(max_length=100, verbose_name='نام خانوادگی مسئول قرارگاه')
    nationality_code = models.CharField(max_length=100, verbose_name='کد ملی مسئول قرارگاه')
    date = models.DateField(verbose_name='تاریخ تولد مسئول قرارگاه')
    phone = models.CharField(max_length=11, verbose_name='تلفن مسئول قرارگاه')
    adress = models.CharField(max_length=400, verbose_name='آدرس قرارگاه')
    number_sa = models.CharField(max_length=11, verbose_name='شماره ثابت قرارگاه')
    date_created = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ساخت قرارگاه')
    hovze = models.CharField(max_length=150, verbose_name='حوزه فعالیت قرارگاه')
    payam = models.CharField(max_length=150, verbose_name='پیام رسان مورد استفاده قرارگاه')

    def __str__(self) -> str:
        return self.username


class MyUserManager(BaseUserManager):
    def create_user(self, nationality_code, group_name, admin_name, admin_lastname, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        user = self.model(
            nationality_code=nationality_code,
            group_name=group_name,
            admin_name=admin_name,
            admin_lastname=admin_lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nationality_code, group_name, password, admin_lastname, admin_name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            nationality_code,
            password=password,
            group_name=group_name,
            admin_name=admin_name,
            admin_lastname=admin_lastname,
        )
        user.is_admin = True
        user.is_active_on_panel = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    nationality_code = models.CharField(
        verbose_name='کد ملی مسئول گروه',
        max_length=100,
        unique=True,
    )

    group_name = models.CharField(
        verbose_name=' نام گروه',
        max_length=100,
        unique=True,
    )
    admin_name = models.CharField(
        verbose_name=' نام گروه',
        max_length=100,
    )
    admin_lastname = models.CharField(
        verbose_name=' نام گروه',
        max_length=100,
    )
    group_name = models.CharField(unique=True, max_length=100 , verbose_name="نام گروه جهادی")
    nationality_code = models.CharField(max_length=100,unique=True , verbose_name="کد ملی")
    admin_name = models.CharField(max_length=100 , verbose_name="نام مسئول گروه جهادی")
    admin_lastname = models.CharField(max_length=100 , verbose_name="نام خانوادگی مسئول گروه جهادی")

    is_active = models.BooleanField(default=True , verbose_name="گروه جهادی فعال است و اجازه ورود دارد")
    is_admin = models.BooleanField(default=False , verbose_name=" گروه جهادی مدیر سایت است")
    is_active_on_panel = models.BooleanField(default=False , verbose_name="گروه جهادی می تواند به پنل کاربری دسترسی داشته باشد")

    objects = MyUserManager()

    USERNAME_FIELD = 'nationality_code'
    REQUIRED_FIELDS = ['group_name', 'admin_name', 'admin_lastname']

    def __str__(self):
        return self.nationality_code

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Group(models.Model):
    gharargah =models.ManyToManyField(Garargah,related_name="group",verbose_name='قرارگاه')
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='Group',verbose_name='گروه جهادی',null=False, blank=False)
    date = models.CharField(max_length=10,verbose_name='تاریخ تولد مسئول گروه جهادی',null=False, blank=False)
    phone = models.CharField(max_length=11,verbose_name='شماره تلفن مسئول گروه جهادی',null=False, blank=False)
    adress = models.CharField(max_length=400,verbose_name='ادرس دفتر گروه جهادی',null=True, blank=True)
    number_sa = models.CharField(max_length=11,verbose_name='شماره ثابت گروه جهادی',null=False, blank=False)
    date_created = models.CharField(max_length=10,verbose_name='تاریخ ساخت گروه جهادی' ,null=False, blank=False)
    farhangi = models.BooleanField(default=False ,verbose_name='فرهنگی')
    hjtmayi = models.BooleanField(default=False ,verbose_name='اجتماعی')
    amizeshi = models.BooleanField(default=False ,verbose_name='آموزشی')
    kshavarzi = models.BooleanField(default=False ,verbose_name='کشاورزی')
    omrani = models.BooleanField(default=False ,verbose_name='عمرانی')
    all = models.BooleanField(default=False ,verbose_name='تمام حوضه ها')
    eta = models.BooleanField(default=False ,verbose_name='ایتا')
    rubika = models.BooleanField(default=False,verbose_name='روبیکا')
    bale = models.BooleanField(default=False,verbose_name='بله')
    srosh = models.BooleanField(default=False,verbose_name='سروش')
    tel = models.BooleanField(default=False,verbose_name='تلگرام')
    inesta = models.BooleanField(default=False ,verbose_name='اینستاگرام')


    def __str__(self):
        return self.user.group_name
    def save_group_user(sender, **kwargs):
        if kwargs['created']:
            group_user = Group(user=kwargs['instance'])
            group_user.save()

    post_save.connect(save_group_user, sender=MyUser)

