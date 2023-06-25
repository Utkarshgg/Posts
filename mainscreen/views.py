from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from mainscreen.models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .forms import PostForm
from django.contrib import messages

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
    posts = Post.objects.filter(is_deleted = False, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_edit(request, user_id):
    post = get_object_or_404( Post, user_id = user_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post =  form.save(commit=False)
            post.user = request.user
            post.timestamp = timezone.now()
            post.save()
            return redirect('blogHome')
        else:
            form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
# def post_new(request):
#         print(request.method)
#         if request.method == "GET":
                
#             if request.user.is_authenticated:
#                 print("YES")
#                 form = PostForm(request.POST)
#                 for field in form:
#                     print("Field Error:", field.name,  field.errors)
#                     messages.error(request, field.errors)
#                 if form.is_valid():
#                     print("YESgg")
#                     userr = User.objects.get(username=request.user)
#                     post = form.save(commit=False)
#                     post.user = userr
#                     post.timestamp = timezone.now()
#                     post.save()
#                     # return redirect('blog/post_edit.html', pk=post.pk)
#                     print("Post has been created")
#                     return render(request,'post_edit', {'form': form})
#             else:
#                 # return HttpResponse("Please Login to Continue") 
#                 return redirect('blogHome')
                   
#         else:
#             print("NOI")
#             form = PostForm()
#             return render(request, 'blog/post_edit.html', {'form': form})
        
#         return render(request, 'blog/post_edit.html')

def blogHome1(request, user_id):
    user = get_object_or_404(User, id = user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'blog/blogHome1.html', {'posts': posts})
    # return HttpResponse("This is blog home area")


def delete_Post(request, sno ):
    print("yes")
    post = get_object_or_404( Post, sno = sno)
    post.is_deleted = True
    post.save()
    return render(request, 'blog/blogHome.html')


def postme(request):


  if request.user.is_authenticated:
    if request.method == "POST":
        print('yes')
        title = request.POST['title']
        description = request.POST['Description']
        isdeleted = False
        timestamp = timezone.now()
        user = request.user

        if len(title)<2 or len(description)<3:
            messages.error(request, 'Please enter the details correctly')
        else:
            post = Post(title=title, description=description, is_deleted=isdeleted, timestamp=timestamp, user=user)
            print(post)
            post.save()
            messages.success(request, 'Your Post has been posted successfully') 

    return render(request,'blog/post_edit.html')
  else:
      return HttpResponse("Please Login to Continue")
 














