from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from djs.models import Post
from datetime import datetime
# def homepage(request):
#     posts = Post.objects.all()
#     post_lists=list()
#     for count, post in enumerate(posts):
#         post_lists.append('No.{}:'.format(str(count))+str(post)+'<br>')
#         post_lists.append('<small>'+str(post.body.encode('utf-8'))+'</small><br><hr>')
#     return HttpResponse(post_lists)

def homepage(request):
    posts=Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    try:
        post=Post.objects.get(slug=slug)
        if post!=None:
            return render(request,'post.html',locals())
    except:
        return redirect('/')