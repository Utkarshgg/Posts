from django.shortcuts import render,HttpResponse
from mainscreen.models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def blogHome(request):
    posts = Post.objects.all()
    print(posts)
    context = {'posts': posts}
    return render(request, 'blog/blogHome.html',context)
    # return HttpResponse("This is blog home area")

def blogPost(request, slug):
    posts = Post.objects.all()
    print(posts)
    context = {'posts': posts}
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f'This is Blog Posts area : {slug}')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})









