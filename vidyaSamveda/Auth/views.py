from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return HttpResponse("WELCOME")

def login(request):
    return render(request,"index.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    return render(request,"signup.html")


def forgot_password(request):
    return render(request,"forgot_pass.html")

def intern_post(request):
    return render(request,"intern_post.html")

def signin(request):
	if request.method == 'POST':
		email = request.POST['email']
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		if password == confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username is already taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email is already used')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save()
		else:
			messages.info(request,'password doesnot match')
			return redirect('register')
		return redirect('login')
	
	else:
		user = request.user
		if user.is_authenticated:
			return redirect('/')
		else:
			return render(request,'st_regis.html')


def recruit_regis(request):
    return render(request,"recruit_regis.html")

def internship_view(request):
    return render(request,"internship_view.html")
