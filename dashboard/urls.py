from django.urls import path

from . import views

urlpatterns=[
	path('',views.admin_home,name='admin_home'),
	path('add-skills',views.add_skills,name='add_skills'),
	path('add-skills/<int:id>',views.edit_skills,name='edit_skills'),
	path('delete-skill/<int:id>',views.delete_skills,name='delete_skills'),


]