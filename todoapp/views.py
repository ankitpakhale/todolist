from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.

def userSignUp(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)
        Password = request.POST['password']
        print(Password)
        ConfirmPassword = request.POST['confirmPassword']
        print(ConfirmPassword)

        try:
            if ConfirmPassword == Password:
                v = signUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.confirmPassword = ConfirmPassword
                v.save()
                return redirect('LOGIN')
            else:
                msg = 'Enter Same Password'
                return render(request , 'signup.html',{'msg':msg}) 

        finally:
            messages.success(request, 'Signup Successfully Done...')

    return render(request,'signup.html')

def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            check = signUp.objects.get(email = em)
            print("Email is ",em)
            if check.password == pass1:
                request.session['email'] = check.email
                print('User successfully logged in')
                return redirect('DASHBOARD')
            else:
                msg = 'Invalid Password'
                return render(request , 'login.html',{'msg':msg}) 
        except:
            msg = 'Invalid Email ID'
            return render(request,'login.html', {'msg':msg})
    return render(request,'login.html')

def dashboard(request):
    if 'email' in request.session:
        user = signUp.objects.get(email=request.session['email'])
    
        if request.POST:
            title = request.POST['title']
            print(title)
            description = request.POST['description']
            print(description)
            if len(title) >= 100:
                messages.error(request, 'Title should be less than or equal to 100 characters')

            if len(description) >= 1000:
                messages.error(request, 'Description should be less than or equal to 1000 characters')  

            if len(title) <= 100 and len(description) <= 1000:
                db = TodoList()
                db.title = title
                db.description = description  
                db.owner = user      
                db.save()
            
            return HttpResponseRedirect('http://127.0.0.1:8000/')

        card = TodoList.objects.filter(owner=user)

        return render(request, 'dashboard.html', {'name': user.name, 'card': card})
    return redirect('LOGIN')

def updatecard(request, pk):
    if 'email' in request.session:
        az = TodoList.objects.get(id = pk)
        user = signUp.objects.get(email=request.session['email'])
        card = TodoList.objects.filter(owner = user)

        print(card)

        if request.POST:
            az.title = request.POST['title']
            az.description = request.POST['description']
            az.save()
            return redirect('DASHBOARD') 
        return render(request, 'dashboard.html', {'az': az, 'name': user.name, 'card': card})

    return redirect('LOGIN')


def deletecard(request,pk):
    if 'email' in request.session:
        prod= get_object_or_404(TodoList, pk=pk)   
        prod.delete() 
        return(redirect('DASHBOARD'))
    return redirect('LOGIN')


def userLogOut(request):
    del request.session['email']
    print('User successfully logged out')
    return redirect('LOGIN')