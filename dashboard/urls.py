from django.urls import path

from . import views

urlpatterns=[
	path('',views.admin_home,name='admin_home'),

	#additonal infromation
	path('add-AddinalInfo',views.additional_info,name='additional_info'),
	path('edit-AddtionalInfo',views.edit_additional_info,name='edit_additional_info'),

	#skills
	path('add-skills',views.add_skills,name='add_skills'),
	path('add-skills/<int:id>',views.edit_skills,name='edit_skills'),
	path('delete-skill/<int:id>',views.delete_skills,name='delete_skills'),
	#educations
	path('add-education',views.add_education,name='add_education'),
	path('edit-education/<int:id>',views.edit_education,name='edit_education'),
	path('delete-education/<int:id>',views.delete_education,name='delete_education'),
	#work exprience
	path('add-work_exp',views.add_work_exp,name='add_work_exp'),
	path('edit-work_exp/<int:id>',views.edit_work_exp,name='edit_work_exp'),
	path('delete-work_exp/<int:id>',views.delete_work_exp,name='delete_work_exp'),

	#reviews
	path('add-reviews',views.add_reviews,name='add_reviews'),
	path('edit-reviews/<int:id>',views.edit_reviews,name='edit_reviews'),
	path('delete_reviews/<int:id>',views.delete_reviews,name='delete_reviews'),
	



]