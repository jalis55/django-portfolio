from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login-user',views.login_user,name='login_user'),
    path('logout-user',views.logout_user,name='logout_user'),
    
]
