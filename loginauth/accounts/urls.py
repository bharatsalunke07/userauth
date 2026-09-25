from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("verify-email/", views.verify_email, name="verify_email"),

    path(
    "password-reset/",
    auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"
    ),
    name="password_reset",
),

path(
    "password-reset/done/",
    auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ),
    name="password_reset_done",
),

path(
    "password-reset-confirm/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html"
    ),
    name="password_reset_confirm",
),

path(
    "password-reset-complete/",
    auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ),
    name="password_reset_complete",
),
    
    path(
    "resend-otp/",
    views.resend_otp,
    name="resend_otp",
),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
    "delete-account/",
    views.delete_account,
    name="delete_account",
),
    path("logout/", views.user_logout, name="logout"),
]