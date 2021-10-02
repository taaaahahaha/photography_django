from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

CURRENT_USER = None


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):

    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        auth = "Notlogged"

        context={}

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                auth = "Logged"
                global CURRENT_USER
                CURRENT_USER = user.id
                context['user']=user
                pass
            else:
                auth = "Passwordincorrect"
        except:
            auth = "Emailincorrect"

        context['auth']=auth

        return render(request,'index.html',context)


    return render(request,'login.html')

def signup(request):

    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        studioname = request.POST['studioname']
        facebook_id = request.POST['facebook_id']
        instagram_id = request.POST['instagram_id']
        postal_address = request.POST['postal_address']
        # price = request.POST['price']
        price = 0

        new_user = User(
            fname=fname,
            lname=lname,
            email=email,
            password=password,
            studioname=studioname,
            facebook_id=facebook_id,
            instagram_id=instagram_id,
            postal_address=postal_address,
            price=price
            )
        new_user.save()

        return redirect('/')

    return render(request,'signup.html')


def update(request):
    newuser = User.objects.get(id=CURRENT_USER)
    context={
        'fname': newuser.fname,
        'lname': newuser.lname ,
        'email': newuser.email, 
        'password': newuser.password,
        'postal_address': newuser.postal_address,
        'studioname':  newuser.studioname,
        'price': newuser.price,
        'instagram_id':  newuser.instagram_id,
        'facebook_id':  newuser.facebook_id,
    }
    if request.method == "POST":
        return render(request,'update.html',context)
    else:
        return HttpResponse("Cheeky")

def nupdate(request,pk):
    newuser = User.objects.get(id=CURRENT_USER)
    context={
        'pk':pk,
        'fname': newuser.fname,
        'lname': newuser.lname ,
        'email': newuser.email, 
        'password': newuser.password,
        'postal_address': newuser.postal_address,
        'studioname':  newuser.studioname,
        'price': newuser.price,
        'instagram_id':  newuser.instagram_id,
        'facebook_id':  newuser.facebook_id,
    }
    
    return render(request,'update.html',context)
    

def main(request):
    newuser = User.objects.get(id=CURRENT_USER)
    context={
        'fname': newuser.fname,
        'lname': newuser.lname ,
        'email': newuser.email, 
        'password': newuser.password,
        'postal_address': newuser.postal_address,
        'studioname':  newuser.studioname,
        'price': newuser.price,
        'instagram_id':  newuser.instagram_id,
        'facebook_id':  newuser.facebook_id,
        'visit':'False'
    }

    if request.method=="POST":
        return render(request,'usermain.html',context)
    else:
        return HttpResponse("Haha, trying to be cheeky?")


def mainvisit(request,pk):
    newuser = User.objects.get(id=pk)
    context={
        'fname': newuser.fname,
        'lname': newuser.lname ,
        'email': newuser.email, 
        'password': newuser.password,
        'postal_address': newuser.postal_address,
        'studioname':  newuser.studioname,
        'price': newuser.price,
        'instagram_id':  newuser.instagram_id,
        'facebook_id':  newuser.facebook_id,
        'visit':'True'
    }

    if request.method=="POST":
        return render(request,'usermain.html',context)
    else:
        return HttpResponse("Haha, trying to be cheeky?")
   
def new(request):
    return render(request, 'new.html')

def edit(request):
    user = User.objects.get(id=CURRENT_USER)
    print(id,type(id))
    context={
        'fname': user.fname,
        'lname': user.lname ,
        'email': user.email, 
        'password': user.password,
        'postal_address': user.postal_address,
        'studioname':  user.studioname,
        'price': user.price,
        'instagram_id':  user.instagram_id,
        'facebook_id':  user.facebook_id,
        }

    if request.method=="POST":
        user.studioname = request.POST['studio']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.postal_address = request.POST['postal_address']
        user.instagram_id = request.POST['instagram_id']
        user.facebook_id = request.POST['facebook_id']
        user.save()

        context['studioname'] = user.studioname
        context['email'] = user.email
        context['password'] = user.password
        context['postal_address'] = user.postal_address
        context['instagram_id'] = user.instagram_id
        context['facebook_id'] = user.facebook_id
        
        return redirect('/dashboard')
        # return render(request, 'update.html', context)

    return render(request, 'update.html', context)

def dashboard(request):
    
    user=User.objects.all()
    return render((request), 'dashboard.html',{'users':user})
    


def dashboardvisit(request,pk):
    if request.method=='POST':
        print('visit',pk,type(pk))
        newuser = User.objects.get(id=pk)
       
        context={
            'fname': newuser.fname,
            'lname': newuser.lname ,
            'email': newuser.email, 
            'password': newuser.password,
            'postal_address': newuser.postal_address,
            'studioname':  newuser.studioname,
            'price': newuser.price,
            'instagram_id':  newuser.instagram_id,
            'facebook_id':  newuser.facebook_id,
            'visit': 'True',
        }
        return render(request,'usermain.html',context)
    else:
        return HttpResponse("Haha, trying to be cheeky?")
