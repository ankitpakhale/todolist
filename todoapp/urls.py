from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.userSignUp, name='SIGNUP'),
    
    path('login/', views.userLogin, name='LOGIN'),

    path('logout/', views.userLogOut, name='LOGOUT'),
    
    path('dash/', views.dashboard, name='DASHBOARD'), 

    path('update/<int:pk>', views.updatecard, name='update-card'), 
    
    path('deletecard/<int:pk>', views.deletecard, name='delete-card'),


]
