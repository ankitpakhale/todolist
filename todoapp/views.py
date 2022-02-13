from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.

def test(request):
    if 'email' in request.session:
        user = signUp.objects.get(email=request.session['email'])
        return render(request, 'dashboard.html', {'name': user.name})
    return redirect('LOGIN')

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
      
        print("Inside first try block", em)
        check = signUp.objects.get(email = em)
        print("Email is ",em)
        if check.password == pass1:
            request.session['email'] = check.email
            print(f'{check.name} Successfully logged in')
            return redirect('TEST')
        else:
            return HttpResponse('Invalid Password')
    return render(request,'login.html')




def userLogOut(request):
    del request.session['email']
    print('User logged out')
    return redirect('LOGIN')