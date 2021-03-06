from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from dashboard.models import Skills,Education,Reviews,WorkExprience,BasicInfo

# Create your views here.
def home(request):
	skills=Skills.objects.all()
	educations=Education.objects.all().order_by('-id')
	reviews=Reviews.objects.all().order_by('-id')[:3]
	work_exps=WorkExprience.objects.all().order_by('-id')
	basic_info=BasicInfo.objects.get()  

	return render(request,'front_end/index.html',{'skills':skills,'educations':educations,'reviews':reviews,\
		'work_exps':work_exps,'basic_info':basic_info})

	

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