from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('forgot-password/', views.forgot_password__change_email, {'parent_url': 'forgot_password'}, name="forgot_password"),
    path('verify-otp/', views.verify_otp, name="verify_otp"),
    path('create-new-password/', views.create_new_password__email, name="create_new_password"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('change-email/', views.forgot_password__change_email, {'parent_url': 'change_email'}, name="change_email"),
    path('create-new-email/', views.create_new_password__email, name="create_new_email"),
    path('change-password/', views.change_password, name="change_password"),
]