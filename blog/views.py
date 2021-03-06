from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class blogView(View):
    def get(self,request,*args, **kwargs):
        post_data=Post.objects.order_by('-id')
        return render(request,'blog/blog.html',{
            'post_data':post_data
        })
class toiawaseView(View):
    def get(self,request,*args, **kwargs):
        post_data=Post.objects.order_by('-id')
        return render(request,'blog/toiawase.html',{
            'post_data':post_data
        })

class PostDetailView(View):
    def get(self,request,*args, **kwargs):
        post_data=Post.objects.get(id=self.kwargs['pk'])
        return render(request,'blog/post_detail.html',{'post_data':post_data})

class CreatePostView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        form=PostForm(request.POST or None)
        return render(request,'blog/post_form.html',{
            'form':form
        })
    def post(self,request,*args, **kwargs):
        form=PostForm(request.POST or None)
        
        if form.is_valid():
            post_data=Post()
            post_data.author=request.user
            post_data.title=form.cleaned_data['title']
            post_data.content=form.cleaned_data['content']

            if request.FILES:
                post_data.image=request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', post_data.id)

        return render(request,'blog/post_form.html',{
            'form':form
        })