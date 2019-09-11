from django.urls import path

from . import views

urlpatterns=[
	path('',views.admin_home,name='admin_home'),
	#skills
	path('add-skills',views.add_skills,name='add_skills'),
	path('add-skills/<int:id>',views.edit_skills,name='edit_skills'),
	path('delete-skill/<int:id>',views.delete_skills,name='delete_skills'),
	#educations
	path('add-education',views.add_education,name='add_education'),
	path('edit-education/<int:id>',views.edit_education,name='edit_education'),
	path('delete-education/<int:id>',views.delete_education,name='delete_education'),

	#reviews


]