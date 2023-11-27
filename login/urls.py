from django.urls import path
from .views import *
app_name = 'login'
urlpatterns = [
    path('register/', Register, name="register"),    
    path('login/', Login, name="login"),
    path('logout/', Logout_view, name="logout"),
    # path('groupupdate/', GroupUpdate, name="groupupdate"),

]
