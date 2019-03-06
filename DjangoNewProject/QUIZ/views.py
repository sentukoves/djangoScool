from django.shortcuts import render, redirect
from django.http import HttpResponse
from os import urandom
# Create your views here.
from .form import UseForm

SECRET_KEY = urandom(24)

def index(request):
    data = {"form": UseForm}

    if request.method == "POST"  and request.POST.get("Login") and request.POST.get("Password"):
        login , password = request.POST.get("Login"), request.POST.get("Password")
        if login == "admin" and password == "admin":
            request.session.set_expiry(60)
            request.session['pause'] = True
            return redirect("main")
        else:
            data["label"] = "Вы вели неверный логин или пароль"
            return render(request, "quiz/index.html", context=data)
    #response.set_cookie('color', "TEST")  #добавить куки.
    return render(request, "quiz/index.html", context=data)

def main(request):
    if "pause" in request.session:
        return HttpResponse("good")
    else:
        return redirect('login')
