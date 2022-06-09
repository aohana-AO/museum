from tkinter import Label
from django import forms

from allauth.account.forms import SignupForm

class ProfileForm(forms.Form):
    first_name=forms.CharField(max_length=30,label='姓')
    last_name=forms.CharField(max_length=30,label='名')
    department=forms.CharField(max_length=30,label='電話番号',required=False)
    address=forms.CharField(max_length=30,label='住所',required=False)

#サインアップのやつ

class SignupUserForm(SignupForm):
    first_name=forms.CharField(max_length=30,label='姓')
    last_name=forms.CharField(max_length=30,label='名')
    
    def save(self, request):
        user=super(SignupUserForm,self).save(request)
        user.first_name=self.cleaned_date['first_name']
        user.last_name=self.cleaned_date['last_name']
        user.save()
        return user

############################################