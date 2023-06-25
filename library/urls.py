from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("library.urls")),        
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick/', views.adminclick_view),
    path('studentclick/', views.studentclick_view),


    path('adminclick/adminsignup/', views.adminsignup_view),
    path('studentclick/studentsignup/', views.studentsignup_view),
    
    path('adminclick/adminlogin/', LoginView.as_view(template_name='library/adminlogin.html')),
    path('adminclick/adminsignup/adminlogin/', LoginView.as_view(template_name='library/adminlogin.html')),
    
    path('studentclick/studentlogin/', LoginView.as_view(template_name='library/studentlogin.html')),
    path('studentclick/studentsignup/studentlogin/', LoginView.as_view(template_name='library/studentlogin.html')),
    
    path('logout/', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin/', views.afterlogin_view),

    path('afterlogin/addbook/', views.addbook_view),
    path('afterlogin/viewbook/', views.viewbook_view),
    path('afterlogin/issuebook/', views.issuebook_view),
    path('afterlogin/viewissuedbook/', views.viewissuedbook_view),
    path('afterlogin/viewstudent/', views.viewstudent_view),
    path('afterlogin/viewissuedbookbystudent/', views.viewissuedbookbystudent),

]