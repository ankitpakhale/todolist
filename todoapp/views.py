from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
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
        
        card = TodoList.objects.filter(owner=user)
            
        if request.POST:
            title = request.POST['title']
            print(title)
            note = request.POST['note']
            print(note)
            
            db = TodoList()
            db.title = title
            db.description = note  
            db.owner = user      
            db.save()
        
        return render(request, 'dashboard.html', {'name': user.name, 'card': card})
    return redirect('LOGIN')

def deletecard(request, pk):
    query = TodoList.objects.get(pk=id)
    query.delete()
    return HttpResponse("Deleted!")


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