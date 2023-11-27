import requests
from django import forms
from .models import *
from django.forms import ModelForm, ModelMultipleChoiceField, ModelChoiceField
from django.contrib.auth.forms import PasswordResetForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget,AdminSplitJalaliDateTime


# class TestForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ('name', 'date', 'date_time')
#
#     def __init__(self, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#         self.fields['date'] = JalaliDateField(label=_('date'), # date format is  "yyyy-mm-dd"
#             widget=AdminJalaliDateWidget # optional, to use default datepicker
#         )



class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_Confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['group_name','admin_name','admin_lastname','nationality_code']




    def clean_password2(self):
        data = self.cleaned_data
        if data['password']:
            raise forms.ValidationError('Passwords are not the same')
        return data['password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_Confirmation'])
        if commit:
            user.save()
        return user

        
