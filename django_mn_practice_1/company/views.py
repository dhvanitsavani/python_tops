from django.shortcuts import render
from django.shortcuts import redirect
from .models import Employee
import re
import random
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        try:
            user = Employee.objects.get(email=request.POST['email'])
            msg = "Employee already registered"
            
        except:
            pattern = r"^\w+@\w+\.\w+\s*$"
            if re.match(pattern, request.POST['email']):
                try:
                    if request.POST['password'] == request.POST['cpassword']:
                        Employee.objects.create(
                            name = request.POST['name'],
                            email = request.POST['email'],
                            department = request.POST['department'],
                            mobile = request.POST['mobile'],
                            profile_picture = request.FILES['profile_picture'],
                            password = request.POST['password']
                        )
                        request.session['email'] = request.POST['email']
                        request.session['name'] = request.POST['name']
                        request.session['department'] = request.POST['department']
                        request.session['mobile'] = request.POST['mobile']
                        request.session['profile_picture'] = Employee.objects.get(email=request.POST['email']).profile_picture.url
                        msg = "Employee registered successfully"
                        return render(request, 'index.html', {'msg': msg})
                    else:
                        msg = "Password and Confirm Password don't match"

                except:
                    msg = "Enter All Details"

            else:
                msg = "Enter a Valid Email"
        
        return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'signup.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['name']
        del request.session['departmet']
        del request.session['mobile']
        del request.session['profile_picture']
        msg = "Logged out successfully"
    except:
        msg = "Logged out successfully"
    return render(request, 'index.html', {'msg': msg})

def login(request):
    if request.method == 'POST':
        try:
            user = Employee.objects.get(email=request.POST['email'])
            if request.POST['password'] == user.password:
                request.session['email'] = user.email
                request.session['name'] = user.name
                request.session['department'] = user.department
                request.session['mobile'] = user.mobile
                request.session['profile_picture'] = user.profile_picture.url
                msg = "Employee Logged in successfully"
                return render(request, 'index.html', {'msg': msg})
            else:
                msg = "Incorrect Password"
        except:
            msg = "Incorrect Email"
        return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')
    
def forgot_password__change_email(request, parent_url):
    if request.method == 'POST':
        try:
            user = Employee.objects.get(email=request.POST['email'])
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            request.session['email'] = user.email
            request.session['parent_url'] = parent_url
            address = user.email
            subject = 'Sending OTP'
            message = 'Your OTP for forgot password is '+str(otp)

            if address and subject and message:
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                    return redirect(verify_otp)
                except Exception as e:
                    msg = e
        except:
            msg = "Incorrect Email"
        return render(request, 'forgot_password.html', {'msg': msg})
    else:
        if parent_url == 'forgot_password':
            return render(request, 'forgot_password.html')
        elif parent_url == 'change_email':
            return render(request, 'change_email.html')

def verify_otp(request):
    if request.method == 'POST':
        if int(request.POST['otp']) == int(request.session['otp']):
            if request.session['parent_url'] == 'forgot_password':
                return render(request, 'create_new_password.html')
            elif request.session['parent_url'] == 'change_email':
                return render(request, 'create_new_email.html')
            
        else:
            msg = "Incorrect OTP"
            return render(request, 'verify_otp.html', {'msg': msg})

    else:
        return render(request, 'verify_otp.html')
    
def create_new_password__email(request):
    if request.method == 'POST':
        if request.POST['new_password'] == request.POST['cnew_password']:
            if request.session['parent_url'] == 'change_email':
                pattern = r'^\w+@\w+\.\w+\s*$'
                if re.match(pattern, request.POST['new_email']):
                    if request.POST['new_email'] != request.session['email']:
                        user = Employee.objects.get(email=request.session['email'])
                        request.session['email'] = request.POST['new_email']
                        user.email = request.POST['new_email']
                        user.save()
                    else:
                        msg = "You can't set New Email same as Current Email"
                        return render(request, 'create_new_email.html', {'msg': msg})
                else:
                    msg = "Enter a valid Email"
                    return render(request, 'create_new_email.html', {'msg': msg})
            
            user = Employee.objects.get(email=request.session['email'])
            user.password = request.POST['new_password']
            user.save()

            if request.session['parent_url'] == 'forgot_password':
                request.session['name'] = user.name
                request.session['department'] = user.department
                request.session['mobile'] = user.mobile
                request.session['profile_picture'] = user.profile_picture.url
            msg = "Employee Logged in successfully"
            del request.session['parent_url']
            return render(request, 'index.html', {'msg': msg})
        else:
            msg = "New Password and Confirm Password don't match"
        if request.session['parent_url'] == 'forgot_password':
            return render(request, 'create_new_password.html', {'msg': msg})
        elif request.session['parent_url'] == 'change_email':
            return render(request, 'create_new_email.html', {'msg': msg})
    else:
        if request.session['parent_url'] == 'forgot_password':
            return render(request, 'create_new_password.html')
        elif request.session['parent_url'] == 'change_email':
            return render(request, 'create_new_email.html')

def edit_profile(request):
    if request.method == 'POST':
        user = Employee.objects.get(email=request.session['email'])
        user.name = request.POST['name']
        if request.POST['department'] != '':
            user.department = request.POST['department']
        user.mobile = request.POST['mobile']
        try:
            user.profile_picture = request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['name'] = user.name
        request.session['department'] = user.department
        request.session['mobile'] = user.mobile
        request.session['profile_picture'] = user.profile_picture.url
        msg = "Profile Updated Successfully"
        return render(request, 'index.html', {'msg': msg})
    else:
        return render(request, 'edit_profile.html')
    
def change_password(request):
    if request.method == 'POST':
        user = Employee.objects.get(email=request.session['email'])
        if request.POST['password'] == user.password:
            if request.POST['new_password'] == request.POST['cnew_password']:
                if request.POST['new_password'] != user.password:
                    user.password = request.POST['password']
                    user.save()
                    msg = "Password Changed successfully"
                    return render(request, 'index.html', {'msg': msg})
                else:
                    msg = "You can't set New Password same as Current Password"
            else:
                msg = "New Password and Confirm Password don't match"
        else:
            msg = "Current Password is incorrect"
        return render(request, 'change_password.html', {'msg': msg})
    else:
        return render(request, 'change_password.html')