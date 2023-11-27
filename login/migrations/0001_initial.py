# Generated by Django 4.2.5 on 2023-10-05 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('group_name', models.CharField(max_length=100, unique=True, verbose_name='نام گروه جهادی')),
                ('nationality_code', models.CharField(max_length=100, unique=True, verbose_name='کد ملی')),
                ('admin_name', models.CharField(max_length=100, verbose_name='نام مسئول گروه جهادی')),
                ('admin_lastname', models.CharField(max_length=100, verbose_name='نام خانوادگی مسئول گروه جهادی')),
                ('is_active', models.BooleanField(default=True, verbose_name='گروه جهادی فعال است و اجازه ورود دارد')),
                ('is_admin', models.BooleanField(default=False, verbose_name=' گروه جهادی مدیر سایت است')),
                ('is_active_on_panel', models.BooleanField(default=False, verbose_name='گروه جهادی می تواند به پنل کاربری دسترسی داشته باشد')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Garargah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='نام کاربری قرار گاه(به انگلیسی وارد شود)')),
                ('gharargah_name', models.CharField(max_length=100, verbose_name='نام قرار گاه')),
                ('admin_name', models.CharField(max_length=100, verbose_name='نام مسئول قرارگاه ')),
                ('admin_lastname', models.CharField(max_length=100, verbose_name='نام خانوادگی مسئول قرارگاه')),
                ('nationality_code', models.CharField(max_length=100, verbose_name='کد ملی مسئول قرارگاه')),
                ('date', models.DateField(verbose_name='تاریخ تولد مسئول قرارگاه')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن مسئول قرارگاه')),
                ('adress', models.CharField(max_length=400, verbose_name='آدرس قرارگاه')),
                ('number_sa', models.CharField(max_length=11, verbose_name='شماره ثابت قرارگاه')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ساخت قرارگاه')),
                ('hovze', models.CharField(max_length=150, verbose_name='حوزه فعالیت قرارگاه')),
                ('payam', models.CharField(max_length=150, verbose_name='پیام رسان مورد استفاده قرارگاه')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10, verbose_name='تاریخ تولد مسئول گروه جهادی')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تلفن مسئول گروه جهادی')),
                ('adress', models.CharField(blank=True, max_length=400, null=True, verbose_name='ادرس دفتر گروه جهادی')),
                ('number_sa', models.CharField(max_length=11, verbose_name='شماره ثابت گروه جهادی')),
                ('date_created', models.CharField(max_length=10, verbose_name='تاریخ ساخت گروه جهادی')),
                ('farhangi', models.BooleanField(default=False, verbose_name='فرهنگی')),
                ('hjtmayi', models.BooleanField(default=False, verbose_name='اجتماعی')),
                ('amizeshi', models.BooleanField(default=False, verbose_name='آموزشی')),
                ('kshavarzi', models.BooleanField(default=False, verbose_name='کشاورزی')),
                ('omrani', models.BooleanField(default=False, verbose_name='عمرانی')),
                ('all', models.BooleanField(default=False, verbose_name='تمام حوضه ها')),
                ('eta', models.BooleanField(default=False, verbose_name='ایتا')),
                ('rubika', models.BooleanField(default=False, verbose_name='روبیکا')),
                ('bale', models.BooleanField(default=False, verbose_name='بله')),
                ('srosh', models.BooleanField(default=False, verbose_name='سروش')),
                ('tel', models.BooleanField(default=False, verbose_name='تلگرام')),
                ('inesta', models.BooleanField(default=False, verbose_name='اینستاگرام')),
                ('gharargah', models.ManyToManyField(related_name='group', to='login.garargah', verbose_name='قرارگاه')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to=settings.AUTH_USER_MODEL, verbose_name='گروه جهادی')),
            ],
        ),
    ]