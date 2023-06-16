
from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# User = get_user_model()
    
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
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        print(loginusername, loginpassword)
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            print("login successful")
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handleSignup(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username =  request.POST['username']
       # phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email  = request.POST['email']
        # is_staff = request.POST['forsuperuser', False]
        #tests
        if(len(fname)>2 and len(lname)>2 and pass1==pass2):
            myuser = User.objects.create_user( username, email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
       #     myuser.phone_number = phone
            # if(is_staff=="YES"):
            #     myuser.is_staff = True
            # else:
            #     myuser.is_staff = False
            myuser.save()
            messages.success(request, "Your account has been successfully created")
            return redirect('home')
        else:
            messages.error(request, "Please enter valid credentials")
            return redirect('home')
        #create
    else:
        return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def showthis(request):

    all_users= get_user_model().objects.all()  
    context= {'allusers': all_users}
    return render(request, 'home/home.html', context)






