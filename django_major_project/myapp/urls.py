from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('cycle/', views.cycle, name="cycle"),
    path('news/', views.news, name="news"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('create_new_password/', views.create_new_password, name="create_new_password"),
    path('logout/', views.logout, name="logout"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('add_product/', views.add_product, name="add_product"),
    path('view_product/', views.view_product, name="view_product"),
]