from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='TEST'), 
    
    path('signup/', views.userSignUp, name='SIGNUP'),
    
    path('login/', views.userLogin, name='LOGIN'),

    path('logout/', views.userLogOut, name='LOGOUT'),

]