from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    context = {}
    if request.method == "POST":
        if (request.POST.get("username") and
            request.POST.get("password") and
            request.POST.get("password") == request.POST.get("password_check")
        ):
            new_user = User.objects.create_user(
                username=request.POST.get("username"),
                password=request.POST.get("password")
            )

            auth.login(request, new_user)
            return redirect("market:home")
        else:
            context["error"] = "올바르지 않은 정보입니다."
    return render(request, "accounts/sign-up.html", context)


def log_in(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("password"):
            user = auth.authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )

            if user is not None:
                auth.login(request, user)
                return redirect("market:home")
            else:
                context["error"] = "아이디와 비밀번호를 확인해주세요!"
        else:
            context["error"] = "아이디와 비밀번호를 확인해주세요!"
    return render(request, "accounts/log-in.html", context)


def log_out(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("market:home")