from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse("Working properly..............")

def SignupView(request):
    if request.POST:
       
        Name = request.POST['name']
        Email = request.POST['email']
        
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirmPassword']
        try:
            data = UserDetails2.objects.filter(email=Email)
            if data:
                msg = "Email already registered"
                return render(request, 'signup.html', {'msg': msg})
            elif ConfirmPassword == Password:
                v = UserDetails2()
                v.name = Name
                v.email = Email
                
                v.password = Password
                v.save()
                print(f"{v.name} Signed up successfully")
                
                # getting IPV6 and FE80 address
                # print(netifaces.interfaces())
                # addrs = netifaces.ifaddresses('eno1')
                # # print(addrs)
                # x = addrs.get(10)
                # # (x[0])
                # global_add = x[0].get('addr')
                # print(global_add)
                # link_local = x[2].get('addr')
                # link_local = link_local.replace("%eno1","" )
                # print(link_local)
                # i.ipaddress = global_add+':'+link_local
                IPV6 = requests.get("https://api6.ipify.org", timeout=5).text
                i = IP()
                i.ipaddress = IPV6
                i.save()
                # return HttpResponse(global_add, link_local)

                return redirect('LOGIN2')
            else:
                msg = 'Please Enter Same Password'
                return render(request , 'signup.html',{'msg':msg}) 
        finally:
            messages.success(request, 'Signup Successfully Done...')
    return render(request,'signup.html')

def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
      
        print("Inside first try block", em)
        check = UserDetails2.objects.get(email = em)
        print("Email is ",em)
        if check.password == pass1:
            request.session['email'] = check.email
            print(f'{check.name} Successfully logged in')
            return redirect('DASHBOARD2')
        else:
            return HttpResponse('Invalid Password')
    return render(request,'login.html')
