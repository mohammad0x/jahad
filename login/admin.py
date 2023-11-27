from django.contrib import admin
from .models import *


class MyUserAdmin(admin.ModelAdmin):
    list_display =('group_name','nationality_code','admin_name','admin_lastname')
    list_filter =(['nationality_code'])
    search_fields = ('nationality_code','','group_name','admin_name'  'admin_lastname')

admin.site.register(MyUser ,MyUserAdmin)




class GarargahAdmin(admin.ModelAdmin):
    list_display =('gharargah_name','username' , 'admin_name' ,'phone','adress', 'admin_lastname')
    list_filter =(['username'])
    search_fields = ('gharargah_name','username' , 'admin_name','number_sa','date','hovze','payam','phone','adress' , 'admin_lastname')

admin.site.register(Garargah , GarargahAdmin)






class GroupAdmin(admin.ModelAdmin):
    list_display =('phone' , 'adress' , 'number_sa')
    list_filter =(['user'])
    search_fields = ('phone','adress' ,'date' ,'number_sa' , 'date_created')


admin.site.register(Group , GroupAdmin)




