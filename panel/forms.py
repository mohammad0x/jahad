import requests
from django import forms
from .models import *
from login.models import *

class ArkanUpdateForm(forms.ModelForm):
    class Meta:
        model = Arkan
        fields = [ 'user', 'name', 'last_name', 'semat', 'phone']


class ActivetyUpdateForm(forms.ModelForm):
    class Meta:
        model = Activety
        fields = ['arsefa', 'tedadshe', 'date', 'numberhokm','name_masol','phone_masol','message']



class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [ 'date','phone','adress','number_sa','date_created','all','farhangi','hjtmayi','amizeshi','kshavarzi','omrani','eta','rubika','bale','srosh','tel','inesta']




class GroupCreateForml(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['adress','number_sa','date_created','all','farhangi','hjtmayi','amizeshi','kshavarzi','omrani','eta','rubika','bale','srosh','tel','inesta']





class UserUpForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['admin_name','nationality_code','admin_lastname']



class UserUpFormM(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['phone','date']


class GroupAA(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['gharargah']




