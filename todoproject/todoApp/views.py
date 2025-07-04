from django.shortcuts import render,redirect
from todoApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(req):
    data=todoModel.objects.filter(user=req.user)
    inprogress=todoModel.objects.filter(user=req.user,status='inprogress')
    completed=todoModel.objects.filter(user=req.user,status='completed')
    pending=todoModel.objects.filter(user=req.user,status='pending')

    context={
        'data':data,
        'inprogress':inprogress,
        'completed':completed,
        'pending':pending
    }
    
    return render(req,'homepage.html',context)


def loginpage(req):
    if req.method == "POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            return redirect('homepage')

    return render(req,'loginpage.html')



def registerpage(req):
    if req.method == "POST":
        full_name=req.POST.get('full_name')
        image=req.FILES.get('image')
        email=req.POST.get('email')
        address=req.POST.get('address')
        username=req.POST.get('username')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        city_name=req.POST.get('city_name')
        bio=req.POST.get('bio')
        phone=req.POST.get('phone')

        if password==confirm_password:
            customuserModel.objects.create_user(
                full_name=full_name,
                image=image,
                email=email,
                address=address,
                username=username,
                password=password,
                city_name=city_name,
                bio=bio,
                phone=phone,
            )
            return redirect('loginpage')
            
    return render(req,'registerpage.html')


def logoutpage(req):
    logout(req)
    return redirect('loginpage')

@login_required
def changepassword(req):
    current_user=req.user
    if req.method == 'POST':
        old_password=req.POST.get('old_password')
        new_password=req.POST.get('new_password')
        confirm_password=req.POST.get('confirm_password')
        if check_password(old_password,req.user.password):
            if new_password==confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(req,current_user)
                return redirect('homepage')


    return render(req,'changepassword.html')

@login_required
def addtask(req):
    if req.method == 'POST':
        title=req.POST.get('title')
        description=req.POST.get('description')
        status=req.POST.get('status')

        data=todoModel(
            user=req.user,
            title=title,
            description=description,
            status=status,

        )
        data.save()
        return redirect('tasklist')
    return render(req,'addtask.html')

@login_required
def tasklist(req):
    data=todoModel.objects.filter(user=req.user)
    context={
        'data':data
    }
    
    return render(req,'tasklist.html',context)
@login_required
def editpage(req,id):
    data=todoModel.objects.get(id=id)
    context={
        'data':data
    }
    if req.method == 'POST':
        data.title=req.POST.get('title')
        data.description=req.POST.get('description')
        data.status=req.POST.get('status')
        data.save()
        return redirect('tasklist')

    return render(req,'editpage.html',context)

@login_required
def deletepage(req,id):
    data=todoModel.objects.get(id=id).delete()
    return redirect('tasklist')


@login_required
def viewpage(req,id):
    data=todoModel.objects.get(id=id)
    context={
        'data':data
    }
    
    return render(req,'viewpage.html',context)