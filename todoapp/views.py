from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.

def test(request):
    return HttpResponse("Working properly..............")

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
                nameMsg = signUp.objects.all()
                print('User logged in')
                # return redirect('HOME')
                return render(request,'home.html', {'key':nameMsg})
            else:
                msg = 'Invalid Password'
                return render(request , 'wrongPassword.html',{'msg':msg}) 
        # except(NameError):
        #     return render(request, '404-error-page.html')
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')
        except:
            msg = 'Invalid Email ID'
            return render(request,'wrongPassword.html', {'msg':msg})
    return render(request,'login.html')
