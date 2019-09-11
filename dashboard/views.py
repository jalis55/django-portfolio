from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Skills
import json


# Create your views here.
@login_required(login_url="login_user")
def admin_home(request):
	return render(request,'admin_pages/home.html')
	# return HttpResponse("Hello admin")

@login_required(login_url="login_user")
def add_skills(request):
	if request.method=="POST":
		skill_name=request.POST['skill_name']
		rating=int(request.POST['skill_rating'])
		Skills.objects.create(
			skill_name=skill_name,
			rating=rating
			)
		# return HttpResponse("success":False, status=200)

	skills=Skills.objects.all()
	return render(request,'admin_pages/add_skills.html',{'skills':skills})

@login_required(login_url="login_user")
def edit_skills(request,id):
	if request.method=='POST':
		new_skill_name=request.POST['skill_name']
		new_skill_rating=request.POST['skill_rating']
		skill_data=Skills.objects.get(id=id)
		skill_data.skill_name=new_skill_name
		skill_data.rating=new_skill_rating
		skill_data.save()
		return redirect('add_skills')
	skill=Skills.objects.get(id=id)
	return render(request,'admin_pages/edit_skills.html',{'skill':skill})

@login_required(login_url="login_user")
def delete_skills(request,id):
	Skills.objects.get(id=id).delete()
	return redirect('add_skills')




