from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .forms import PostForm
from .models import Post
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def indexview(request):
    post = Post.objects.all()

    post_paginator = Paginator(post,4)
    page_number = request.GET.get('page')
    page_obj = post_paginator.get_page(page_number)
    context = {
        "page_obj":page_obj
    }
    return render(request, 'announcement/index.html', context)

@login_required(login_url='account_login')
def post_announcements(request):
    form = PostForm()
    post = Post.objects.all()

    if request.method =="POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,'announcement added sucessfully')
        else:
            form = PostForm()
    else:
        return render(request,'announcement/announcements.html')
        
   
    return redirect('review_announcements')
@login_required(login_url='account_login')
def review_announcements(request):
    post = Post.objects.all()

    context = {
        "posts":post
    }
    return render(request, 'announcement/review_announcements.html', context)
def update_announcements(request, pk):
    post = get_object_or_404(Post,pk=pk)
    #pass the object as instance in form
    form = PostForm(request.POST or None, instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('review_announcements')
    context = {
        'form':form
    }
    return render(request,'announcement/update_announcements.html',context)

def delete_announcements(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context ={
        "post":post
    }
    
    if request.method == "POST":
        post.delete()
        return redirect('review_announcements')

    return render(request, 'announcement/delete_announcements.html', context)


    

    
    
