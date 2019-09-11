from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Skills,Education
import json



# Create your views here.
@login_required(login_url="login_user")
def admin_home(request):
	return render(request,'admin_pages/home.html')
	# return HttpResponse("Hello admin")
#skills
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

#educations

def add_education(request):
	if request.method=='POST':
		from_to=request.POST['from_to']
		degree_name=request.POST['degree_name']
		degree_title=request.POST['degree_title']
		instituation=request.POST['instituation']
		about_degree=request.POST['about_degree']

		Education.objects.create(
			from_to=from_to,
			degree_name=degree_name,
			degree_title=degree_title,
			instituation=instituation,
			about_degree=about_degree

			)
		#success='Insertion succeed'
		#return HttpResponse(json.dumps({'mes': success}), content_type="application/json")
	educations=Education.objects.all()
	return render(request,'admin_pages/add_education.html',{'educations':educations})

def edit_education(request,id):
	if request.method=='POST':
		from_to=request.POST['from_to']
		degree_name=request.POST['degree_name']
		degree_title=request.POST['degree_title']
		instituation=request.POST['instituation']
		about_degree=request.POST['about_degree']
		edu_data=Education.objects.get(id=id)

		edu_data.from_to=from_to
		edu_data.degree_name=degree_name
		edu_data.degree_title=degree_title
		edu_data.instituation=instituation
		edu_data.about_degree=about_degree
		edu_data.save()
		return redirect('add_education')



	edu=Education.objects.get(id=id)
	return render(request,'admin_pages/edit_education.html',{'edu':edu})

def delete_education(request,id):
	Education.objects.get(id=id).delete()
	data = {}
	data['something'] = 'useful'

	return redirect('add_education')

