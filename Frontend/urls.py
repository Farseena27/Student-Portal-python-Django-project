from Frontend import views
from django.urls import path



urlpatterns=[
    path('signup/',views.Signup, name='signup'),
    path('savesignup/', views.savesignup, name='savesignup'),
    path('login/', views.UserLogin, name='login'),
    path('profilepage/', views.UserProfile, name='profilepage'),
    path('updateprofile/<int:id>/', views.UpdateProfile, name='updateprofile'),



    path('logout/', views.UserLogout, name='logout'),
    path('home/',views.HomePage,name='home'),
    path('about/', views.AboutPage, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('savecontact/',views.savecontact, name='savecontact'),
    path('joblist/', views.Joblist, name='joblist'),
    path('jobsingle/<int:jobid>/', views.Jobsingle, name='jobsingle'),
    path('savejobapplications/', views.savejobapplications, name='savejobapplications'),


    # path('joblist/<indus>', views.Joblist, name='joblist'),
    # path('jobsingle/<int:jobid>/', views.JobSingle, name='jobsingle'),
    path('courses/<course_cat>',views.Courselist,name='courses'),
    path('coursesingle/<int:cid>/', views.CourseSingle, name='coursesingle'),
    path('jobapplications/', views.JobApplications, name='jobapplications'),
    path('jobsearch', views.Jobsearch, name='jobsearch')

]