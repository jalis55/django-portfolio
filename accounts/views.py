from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def home(request):
	return render(request,'front_end/index.html')

def login_user(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("admin_home")
		else:
			messages.info(request,"Invalid username or password")
			return redirect("login_user")
		#return HttpResponse(username)
	
	return render(request,"auth_pages/login.html")

def logout_user(request):
	auth.logout(request)
	return redirect("login_user")