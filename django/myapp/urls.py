from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('change-password/', views.change_password, name="change_password"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('verify-otp/', views.verify_otp, name="verify_otp"),
    path('create-new-password/', views.create_new_password, name="create_new_password"),
]