from django.urls import path
from .views import *

app_name = 'panel'

urlpatterns = [
    path('panel/', Panel, name="panel"),
    path('groupupdate/', GroupUpdate, name="groupupdate"),
    path('adminupdate/', AdminUpdate, name="adminupdate"),
    path('arkanupdate/', ArkanUpdate, name="arkanupdate"),
    path('activetyupdate/', ActivetyUpdate, name="activetyupdate"),
    path('contact_to_admin/', Contact_To_admin, name="contact_to_admin"),
    path('payam/', Payam, name="payam"),
    path('',home,name="home"),
    path('dastrasi',dastrasi,name="dastrasi"),
    path('groupupdatetow/',GroupUpdateTow,name="groupupdatetow"),


]
