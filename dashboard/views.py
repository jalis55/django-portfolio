from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Skills,Education,WorkExprience,Reviews,BasicInfo
import json



# Create your views here.

def additional_info(request):
	if request.method=='POST':
		full_name=request.POST['full_name']
		title=request.POST['title']
		email=request.POST['email']
		age=request.POST['age']
		phone=request.POST['phone']
		address=request.POST['address']
		languages=request.POST['languages']
		about=request.POST['about']
		
		#add into additional informantion
		BasicInfo.objects.create(

			full_name=full_name,
			title=title,
			email=email,
			age=age,
			phone=phone,
			address=address,
			languages=languages,
			about=about,
			
			

			)
		return redirect('admin_home')

	return render(request,'admin_pages/additional_info.html')


def edit_additional_info(request):
	if not BasicInfo.objects.filter().exists():
		return redirect('additional_info')
	else:
		if request.method=='POST':
			full_name=request.POST['full_name']
			title=request.POST['title']
			info_id=request.POST['id']
			email=request.POST['email']
			age=request.POST['age']
			phone=request.POST['phone']
			address=request.POST['address']
			languages=request.POST['languages']
			about=request.POST['about']

			#update Additional info
			addi_info=BasicInfo.objects.get(id=info_id)
			addi_info.full_name=full_name
			addi_info.title=title
			addi_info.email=email
			addi_info.age=age
			addi_info.phone=phone
			addi_info.address=address
			addi_info.languages=languages
			addi_info.about=about
			addi_info.save()

			return redirect('edit_additional_info')

		basic_info=BasicInfo.objects.get()
		return render(request,'admin_pages/edit_additional_info.html',{'basic_info':basic_info})










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
		#add skill
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
		#edit skill
		skill_data=Skills.objects.get(id=id)
		skill_data.skill_name=new_skill_name
		skill_data.rating=new_skill_rating
		skill_data.save()
		return redirect('add_skills')
	skill=Skills.objects.get(id=id)
	return render(request,'admin_pages/edit_skills.html',{'skill':skill})

@login_required(login_url="login_user")
def delete_skills(request,id):
	#delete skill
	Skills.objects.get(id=id).delete()
	return redirect('add_skills')

#educations
@login_required(login_url="login_user")
def add_education(request):
	if request.method=='POST':
		from_to=request.POST['from_to']
		degree_name=request.POST['degree_name']
		degree_title=request.POST['degree_title']
		instituation=request.POST['instituation']
		about_degree=request.POST['about_degree']

		#add into education
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
@login_required(login_url="login_user")
def edit_education(request,id):
	if request.method=='POST':
		from_to=request.POST['from_to']
		degree_name=request.POST['degree_name']
		degree_title=request.POST['degree_title']
		instituation=request.POST['instituation']
		about_degree=request.POST['about_degree']
		edu_data=Education.objects.get(id=id)


		#edit education
		edu_data.from_to=from_to
		edu_data.degree_name=degree_name
		edu_data.degree_title=degree_title
		edu_data.instituation=instituation
		edu_data.about_degree=about_degree
		edu_data.save()
		return redirect('add_education')



	edu=Education.objects.get(id=id)
	return render(request,'admin_pages/edit_education.html',{'edu':edu})
@login_required(login_url="login_user")
def delete_education(request,id):
	#delete educations
	Education.objects.get(id=id).delete()
	data = {}
	data['something'] = 'useful'

	return redirect('add_education')


#work exprience
@login_required(login_url="login_user")
def add_work_exp(request):
	if request.method=='POST':
		from_to=request.POST['from_to']
		organization=request.POST['organization']
		job_title=request.POST['job_title']
		job_description=request.POST['job_description']

		#add into work exprience
		WorkExprience.objects.create(
			from_to=from_to,
			organization=organization,
			job_title=job_title,
			job_description=job_description
			)
	works=WorkExprience.objects.all()
	return render(request,'admin_pages/add_work_exp.html',{'works':works})
@login_required(login_url="login_user")
def edit_work_exp(request,id):

	if request.method=='POST':
		from_to=request.POST['from_to']
		organization=request.POST['organization']
		job_title=request.POST['job_title']
		job_description=request.POST['job_description']
		#edit work exprience
		work_data=WorkExprience.objects.get(id=id)
		work_data.from_to=from_to
		work_data.organization=organization
		work_data.job_title=job_title
		work_data.job_description=job_description
		work_data.save()
		return redirect('add_work_exp')

	work_exp=WorkExprience.objects.get(id=id)
	return render(request,'admin_pages/edit_work_exp.html',{'work_exp':work_exp})
@login_required(login_url="login_user")
def delete_work_exp(request,id):
	#delete work exprience
	WorkExprience.objects.get(id=id).delete()
	return redirect('add_work_exp')

#Reviews
def add_reviews(request):
	if request.method=='POST':
		clients_name=request.POST['clients_name']
		organization=request.POST['organization']
		review_description=request.POST['review_description']
		#add into review
		Reviews.objects.create(
			clients_name=clients_name,
			organization=organization,
			review_description=review_description
			)

	reviews=Reviews.objects.all()
	return render(request,'admin_pages/add_reviews.html',{'reviews':reviews})


@login_required(login_url="login_user")
def edit_reviews(request,id):
	if request.method=='POST':
		clients_name=request.POST['clients_name']
		organization=request.POST['organization']
		review_description=request.POST['review_description']
		#updating review data
		review_data=Reviews.objects.get(id=id)
		review_data.clients_name=clients_name
		review_data.organization=organization
		review_data.review_description=review_description
		review_data.save()
		return redirect('add_reviews')

	review=Reviews.objects.get(id=id)
	return render(request,'admin_pages/edit_reviews.html',{'review':review})

@login_required(login_url="login_user")
def delete_reviews(request,id):
	#delete review
	Reviews.objects.get(id=id).delete()
	return redirect('add_reviews')
