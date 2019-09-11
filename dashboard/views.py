from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login_user")
def admin_home(request):
	return render(request,'admin_pages/index.html')
	# return HttpResponse("Hello admin")
