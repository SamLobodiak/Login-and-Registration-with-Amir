from django.shortcuts import render, HttpResponse, redirect
from apps.first_app.models import *
from django.utils.crypto import get_random_string
# from django.db import migrations
import re
import hashlib

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    print("***********going through INDEX views***********")

    return render(request, 'first_app/index.html')

def register(request):
    print("***********going through REGISTER**********")

    if len(request.POST['first_name']) < 2:
        return redirect('/')
    elif len(request.POST['last_name']) < 2:
        return redirect('/')
    elif not EMAIL_REGEX.match(request.POST['email']):
        return redirect('/')
    elif len(request.POST['password']) < 9:
        return redirect('/')
    elif (request.POST['password']) != (request.POST['confirm_password']):
        return redirect('/')
    else:
        # print(users().objects.all().values())
        users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password = hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest()),
        print(users.objects.all().values())
        return redirect('/success')

def login(request):
    print("******going through LOGIN***********")

    # print(users.objects.filter(email__contains=request.POST['email']))
    print (request.POST["login_email"])
    print (request.POST["login_password"])


    if users.objects.filter(email=request.POST['login_email']):
        print(users.objects.filter(email=request.POST["login_email"]))
        # this works
        print(hashlib.md5(request.POST['login_password'].encode('utf-8')).hexdigest())

        email_id = users.objects.filter(email=request.POST["login_email"])[0]
        password_id = users.objects.filter(password=hashlib.md5(request.POST['login_password'].encode('utf-8')).hexdigest())[0]

        print(email_id.password)
        print(email_id.id)

        print(password_id.id)

        if password_id.id == email_id.id:
            return redirect('/success')
        else:
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    print("***********going through SUCCESS******")

    return render(request, 'first_app/success.html')
