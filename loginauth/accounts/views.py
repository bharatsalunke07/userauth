from django.contrib.auth.models import User
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail
from django.contrib import messages
from django.utils.crypto import get_random_string

from .models import EmailVerification

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "accounts/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "accounts/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, "accounts/register.html")

        # Create user but keep account inactive
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_active = False
        user.save()

        # Generate 6-digit OTP
        otp = get_random_string(
            length=6,
            allowed_chars="0123456789"
        )

        # Create or update OTP record
        EmailVerification.objects.update_or_create(
            user=user,
            defaults={"otp": otp}
        )

        # Send OTP email
        send_mail(
            subject="Verify Your Email",
            message=f"""
Hello {username},

Your email verification OTP is:

{otp}

This OTP is valid for 10 minutes.

If you did not create this account, please ignore this email.
""",
            from_email=None,
            recipient_list=[email],
        )

        # Temporarily store user ID
        request.session["verification_user_id"] = user.id

        return redirect("verify_email")

    return render(request, "accounts/register.html")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            return render(
                request,
                "accounts/register.html",
                {"error": "Passwords do not match!"}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "accounts/register.html",
                {"error": "Username already exists!"}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/register.html")

def verify_email(request):
    user_id = request.session.get("verification_user_id")

    if not user_id:
        return redirect("register")

    try:
        user = User.objects.get(id=user_id)
        verification = EmailVerification.objects.get(user=user)
    except (User.DoesNotExist, EmailVerification.DoesNotExist):
        return redirect("register")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")

        if verification.is_expired():
            messages.error(
                request,
                "OTP has expired. Please register again."
            )
            return redirect("register")

        if entered_otp == verification.otp:
            user.is_active = True
            user.save()

            verification.delete()

            del request.session["verification_user_id"]

            messages.success(
                request,
                "Email verified successfully. You can now login."
            )

            return redirect("login")

        messages.error(
            request,
            "Invalid OTP. Please try again."
        )

    return render(
        request,
        "accounts/verify_email.html"
    )

def resend_otp(request):
    user_id = request.session.get("verification_user_id")

    if not user_id:
        return redirect("register")

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect("register")

    # Generate a new 6-digit OTP
    otp = get_random_string(
        length=6,
        allowed_chars="0123456789"
    )

    # Replace the old OTP
    EmailVerification.objects.update_or_create(
        user=user,
        defaults={"otp": otp}
    )

    # Send the new OTP
    send_mail(
        subject="Your New Email Verification OTP",
        message=f"""
Hello {user.username},

Your new email verification OTP is:

{otp}

This OTP is valid for 10 minutes.

If you did not request this code, please ignore this email.
""",
        from_email=None,
        recipient_list=[user.email],
    )

    messages.success(
        request,
        "A new OTP has been sent to your email."
    )

    return redirect("verify_email")
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password!"}
        )

    return render(request, "accounts/login.html")

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def home(request):
    return render(request, "accounts/home.html")

def delete_account(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        user = request.user

        # Delete the authenticated user's account
        user.delete()

        # Remove the user's session
        logout(request)

        return redirect("home")

    return redirect("dashboard")


