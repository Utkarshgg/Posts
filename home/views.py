
from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render (request, 'home/contact.html',{})

def about(request):
    # messages.error(request, 'Welcome to the Register Page')
    if(request.method=='POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        if len(name)<2 :
            messages.error(request, 'Please enter your Name correctly')
        elif len(email)<3:
            messages.error(request, 'Please enter your Email correctly')
        elif len(phone)<10:
            messages.error(request, 'Please enter your Phone Number correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone)
            contact.save()
            messages.success(request, 'You have been registered successfully')

    return render(request, 'home/about.html',{})


def issues(request):
    messages.ERROR(request, 'Welcome to the Register Page')
    if(request.method=='post'):
        print('we are using post')
    return render(request, 'home/issues.html')

def freak(request):
    return render(request,'home/freak.html')

def yes(request):
    return HttpResponse("Yes")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginemail=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginemail, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


