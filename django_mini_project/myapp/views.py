from django.shortcuts import render
from .models import Contact, Users
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            remarks = request.POST['remarks']
        )
        msg = "Contact registered successfully"
        contacts = Contact.objects.all().order_by("-id")[:3]
        return render(request, 'contact.html', {'msg': msg, 'contacts': contacts})
    else:
        contacts = Contact.objects.all().order_by("-id")[:3]
        return render(request, 'contact.html', {'contacts': contacts})

def signup(request):
    if request.method == "POST":
        try: 
            Users.objects.get(email=request.POST['email'])
            msg = "Email already Registered"
        except:
            if request.POST['password'] == request.POST['cpassword']:
                Users.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    password = request.POST['password'],
                    profile_picture = request.FILES['profile_picture']
                )
                msg = "Signed Up Successfully"
            else:
                msg = "Password and Confirm Password does not matched"
        return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        try:
            user = Users.objects.get(email=request.POST['email'])
            if request.POST['password'] == user.password:
                request.session['fname'] = user.fname
                request.session['email'] = user.email
                request.session['profile_picture'] = user.profile_picture.url
                msg = "Login successfully"
                return render(request, 'index.html', {'msg': msg})
            else:
                msg = "Password is incorrect"
        except:
            msg = "Emain not found"
        return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')
    
def logout(request):
    try:      
        del request.session['fname']
        del request.session['email']
        del request.session['profile_picture']
        msg = "Logged Out Successfully"
    except:
        msg = "Logges Out Successfully"
    return render(request, 'login.html', {'msg':msg})

def profile(request):
    if request.method == "POST":
        user = Users.objects.get(email=request.session['email'])
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        try:
            user.profile_picture = request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['fname'] = user.fname
        request.session['profile_picture'] = user.profile_picture.url
        msg = "Profile updated successfully"
        return render(request, 'index.html', {'msg': msg})

    else:
        return render(request, 'profile.html')
    
def change_password(request):
    if request.method == 'POST':
        user = Users.objects.get(email=request.session['email'])
        if request.POST['old_password'] == user.password:
            if request.POST['new_password'] == request.POST['cnew_password']:
                user.password = request.POST['new_password']
                user.save()
                msg = "Password Changed successfully"
                del request.session['email']
                return render(request, 'index.html', {'msg': msg})
            else:
                msg = "New Password and Confirm Password does not matched"
                return render(request, 'change_password.html', {'msg': msg})
        else:
            msg = "Old Password is incorrect"
            return render(request, 'change_password.html', {'msg': msg})
        
    else:
        return render(request, 'change_password.html')
    
def forgot_password(request):
    if request.method == 'POST':
        otp = random.randint(1000, 9999)
        address = request.POST['email']
        subject = "OTP to verify email"
        message = "Your OTP to verify email is "+str(otp)

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address,])
                request.session['otp'] = otp
                request.session['email'] = request.POST['email']
                return render(request, 'verify_otp.html')
            except Exception as e:
                msg = e
        else:
            msg = "All fields are required"
        return render(request, 'forgot_password.html')
    else:
        return render(request, 'forgot_password.html')
    
def verify_otp(request):
    if int(request.POST['otp']) == request.session['otp']:
        del request.session['otp']
        return render(request, 'create_new_password.html')
    else:
        msg = "OTP is incorrect"
        return render(request, 'verify_otp.html', {'msg': msg})
    
def create_new_password(request):
    if request.POST['new_password'] == request.POST['cnew_password']:
        user = Users.objects.get(email=request.session['email'])
        user.password = request.POST['new_password']
        user.save()
        del request.session['email']
        msg = "Password Created successfully"
        return render(request, 'login.html', {'msg': msg})
    else:
        msg = "New Password and Confirm Password does not matched"
        return render(request, 'create_new_password.html', {'msg': msg})