from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dashboard, name='DASHBOARD'), 
    
    path('signup/', views.userSignUp, name='SIGNUP'),
    
    path('login/', views.userLogin, name='LOGIN'),

    path('logout/', views.userLogOut, name='LOGOUT'),
    
    path('deletecard/<int:pk>', views.deletecard, name='delete-card'),
]
