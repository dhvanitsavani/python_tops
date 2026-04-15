from django.shortcuts import render
from .models import User, Product
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random

def index(request):
    try:
        user = User.objects.get(email=request.session['email'])
        if user.user_type == 'buyer':
            return render(request, 'index.html')
        else:
            return render(request, 'seller_index.html')
    except:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cycle(request):
    return render(request, 'cycle.html')

def news(request):
    return render(request, 'news.html')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == user.password:
                request.session['email'] = user.email
                request.session['profile_picture'] = user.profile_picture.url

                msg = "Logged in successfully"
                if user.user_type == 'buyer':
                    return render(request, 'index.html', {'msg': msg})
                else:
                    return render(request, 'seller_index.html', {'msg': msg})
            else:
                msg = "Incorrect Password"
        except:
            msg = "Incorrect Email"
        return render(request, 'login.html', {'msg': msg})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Email already Registered"
        except:
            if request.POST['password'] == request.POST['cpassword']:
                try:
                    User.objects.create(
                        fname = request.POST['fname'],
                        lname = request.POST['lname'],
                        mobile = request.POST['mobile'],
                        email = request.POST['email'],
                        password = request.POST['password'],
                        profile_picture = request.FILES['profile_picture'],
                        user_type = request.POST['user_type']
                    )
                    user = User.objects.get(email=request.POST['email'])
                    request.session['email'] = user.email
                    request.session['profile_picture'] = user.profile_picture.url
                    
                    msg = "Signed up successfully"
                    if user.user_type == 'buyer':
                        return render(request, 'index.html', {'msg': msg})
                    else:
                        return render(request, 'seller_index.html', {'msg': msg})
                except:
                    msg = "All Fields are mendatory"
                    return render(request, 'signup.html', {'msg': msg})
            else:
                msg = "Password and Confirm Password don't match"
        return render(request, 'signup.html', {'msg': msg})
    return render(request, 'signup.html')

def forgot_password(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            request.session['email'] = user.email
            address = user.email
            subject = 'Sending OTP'
            message = 'Your OTP for forgot password is '+str(otp)+'.'
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address,])
                return render(request, 'verify_otp.html')
            except Exception as e:
                msg = e
                return render(request, 'forgot_password.html', {'msg': msg})
        except:
            msg = "Incorrect Email"
            return render(request, 'forgot_password.html', {'msg': msg})
    return render(request, 'forgot_password.html')

def verify_otp(request):
    if request.method == 'POST':
        if int(request.POST['otp']) == int(request.session['otp']):
            del request.session['otp']
            return render(request, 'create_new_password.html')
        else:
            msg = "Incorrect OTP"
            return render(request, 'verify_otp.html', {'msg': msg})

def create_new_password(request):
    if request.method == 'POST':
        if request.POST['new_password'] == request.POST['cnew_password']:
            user = User.objects.get(email=request.session['email'])
            user.password = request.POST['new_password']
            user.save()
            request.session['profile_picture'] = user.profile_picture.url
            msg = "Logged in successfully"
            if user.user_type == 'buyer':
                return render(request, 'index.html', {'msg': msg})
            else:
                return render(request, 'seller_index.html', {'msg': msg})
        else:
            msg = "New Password and Confirm New Password don't match"
            return render(request, 'create_new_password.html', {'msg': msg})

def logout(request):
    try:
        del request.session['email'] 
        del request.session['profile_picture']
        msg = "Logged out successfully"
    except:
        msg = "Logged out successfully"
    return render(request, 'index.html', {'msg': msg})

def edit_profile(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.mobile = request.POST['mobile']
        user.user_type = request.POST['user_type']
        try:
            user.profile_picture = request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['profile_picture'] = user.profile_picture.url
        msg = "Profile Updated successfully"

        if user.user_type == 'buyer':
            return render(request, 'index.html', {'msg': msg})
        else:
            return render(request, 'seller_index.html', {'msg': msg})
    if user. user_type == 'buyer':
        return render(request, 'edit_profile.html', {'user': user})
    else:
        return render(request, 'seller_edit_profile.html', {'user': user})
    
def add_product(request):
    if request.method == 'POST':
        seller = User.objects.get(email=request.session['email'])
        try:
            Product.objects.create(
                seller = seller,
                product_category = request.POST['product_category'],
                product_name = request.POST['product_name'],
                product_price = request.POST['product_price'],
                product_desc = request.POST['product_desc'],
                product_image = request.FILES['product_image']
            )
            msg = "Product Added successfully"
            return render(request, 'seller_index.html', {'msg': msg})
        except:
            msg = "All Fields are mendatory"
            return render(request, 'add_product.html', {'msg': msg})
    return render(request, 'add_product.html')

def view_product(request):
    products = Product.objects.filter(seller=User.objects.get(email=request.session['email']))
    return render(request, 'view_product.html', {'products': products})