from ast import For
from logging.config import valid_ident
from re import template
from django.shortcuts import render,redirect
from django.views import View
from accounts.models import CustomUser
from accounts.forms import ProfileForm,SignupUserForm
from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        user_date=CustomUser.objects.get(id=request.user.id)
        return render(request,"accounts/profile.html",{'user_date':user_date,})


class ProfileEditView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        user_date=CustomUser.objects.get(id=request.user.id)
        form=ProfileForm(
            request.POST or None,
            initial={
                'first_name':user_date.first_name,
                'last_name':user_date.last_name,
                'department':user_date.department,
                'address':user_date.address,
            }
        )

        return render(request,'accounts/profile_edit.html',{
            'form':form
        })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)
        if form.is_valid():
            user_date=CustomUser.objects.get(id=request.user.id)
            user_date.first_name=form.cleaned_data['first_name']
            user_date.last_name=form.cleaned_data['last_name']
            user_date.department=form.cleaned_data['department']
            user_date.address=form.cleaned_data['address']
            user_date.save()
            return redirect('profile')
            
        return render(request,'account/profile.html',{
            'form':form
        })

class LoginView(views.LoginView):
    template_name='accounts/login.html'

class LogoutView(views.LogoutView):
    template_name='accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')


##############################
class SignupView(views.SignupView):
    template_name='accounts/signup.html'
    from_class=SignupUserForm

    ###########################