from django.contrib import admin
from .models import *




class ArkanAdmin(admin.ModelAdmin):
    list_display =('name','user','last_name' , 'semat' , 'phone')
    list_filter =(['name'])
    search_fields = ('name','lastname' , 'semat' , 'phone')

admin.site.register(Arkan , ArkanAdmin)





class ActivetyAdmin(admin.ModelAdmin):
    list_display =('arsefa','name_masol' , 'phone_masol' , 'numberhokm')
    list_filter =(['numberhokm'])
    search_fields = ('arsefa','name_masol','date' ,'tedadshe', 'phone_masol' , 'numberhokm')

admin.site.register(Activety , ActivetyAdmin)




class Contact_to_adminAdmin(admin.ModelAdmin):
    list_display =('name','mozo' , 'message')
    list_filter =(['mozo'])
    search_fields = ('name','mozo' ,'publish', 'message')

admin.site.register(Contact_to_admin , Contact_to_adminAdmin)






class Contact_to_userAdmin(admin.ModelAdmin):
    list_display = ('name', 'mozo', 'message')
    list_filter = (['mozo'])
    search_fields = ('name', 'mozo', 'message')

admin.site.register(Contact_to_user , Contact_to_userAdmin)







