from django.urls import path,include
from . import views
from databaseApi.views import *
from users.views import users,admins,coaches,dashboard,Payment,salesReport
from databaseApi.views import change_data,profile_view,addPayment,addEquippment
from users.views import admins,coaches,dashboard,salesReport
from authentication.views import signup,change_Password,verify_token,signup,login, loginForm,logout_view,form_view
from feed.views import addPost,addComment
from Gym.views import Equip
from databaseApi.views import *

urlpatterns = [
                path('login/', loginForm, name='login'),
                path('logout/', logout_view, name='logout'),
                path('form/', form_view),
                path('signup/',signup),
                path('signupform/',signup, name = 'signupform'),
                path('loginform/',login, name = 'loginform'),
                # path('users/',get_Users),
                # path('admin/',get_Profiles),
                # path('coaches/',get_Coaches),
                path('profilesData/',admins,name='profiles'),
                path('changeDataForm/',change_data, name = 'changeDataForm'),
                path('changePasswordForm/',change_Password, name = 'changePasswordForm'),
                
                path('verify-token/', verify_token, name='verify_token'),
                path('Dashoard/',views.user_dashboard, name = 'Dashboard'),
                path('Equip/',Equip, name = 'Equip'),
                path('payment/',Payment, name = 'payment'),
                path('addPayment/',addPayment, name = 'addPayment'),
                path('addPost/',addPost, name = 'addPost'),
                path('addComment/',addComment, name = 'addComment'),
                path('salesReport/',salesReport, name = 'salesReport'),
                path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
                path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
                path('sales-report/', views.sales_report, name='sales_report'),
                path('registerCoach/', check_registered_coach, name='registerCoach'),
                path('register_coach', register_coach, name='register_coach'),
                path('registerNutritionist/', check_registered_nutritionist, name='registerNutritionist'),
                path('register_nutritionist', register_nutritionist, name='register_nutritionist'),
                path('rate-coach/', rate_coach, name='rate_coach'),
                path('rate_nutritionist/', rate_nutritionist, name='rate_nutritionist'),
                path('addEquippment/', addEquippment, name='addEquippment'), 
                
                ]
