from django.urls import path
from Backend import views
urlpatterns=[
    path('admin_loginpage/',views.AdminLogin,name='loginpage'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/',views.AdminHome,name='admin_home'),
    path('index/',views.Index,name='index'),

    path('addcoursecategory/', views.AddCourseCategory, name='addcoursecategory'),
    path('savecoursecategory/', views.savecoursecategory, name='savecoursecategory'),
    path('displaycoursecategory/', views.DisplayCourseCategory, name='displaycoursecategory'),
    path('editcoursecategory/<int:id>/', views.EditCourseCategory, name='editcoursecategory'),
    path('updatecoursecategory/<int:id>/', views.UpdateCoursecategory, name='updatecoursecategory'),
    path('deletecoursecategory/<int:id>/', views.DeleteCourseCategory, name='deletecoursecategory'),

    path('addcourse/', views.AddCourse, name='addcourse'),
    path('savecourse/', views.savecourse, name='savecourse'),
    path('displaycourse/', views.DisplayCourse, name='displaycourse'),
    path('editcourse/<int:id>/', views.EditCourse, name='editcourse'),
    path('updatecourse/<int:id>/', views.UpdateCourse, name='updatecourse'),
    path('deletecourse/<int:id>/', views.DeleteCourse, name='deletecourse'),

    path('addjobcategory/', views.AddJobCategory, name='addjobcategory'),
    path('savejobcategory/', views.savejobcategory, name='savejobcategory'),
    path('displayjobcategory/', views.DisplayJobCategory, name='displayjobcategory'),
    path('editjobcategory/<int:id>/', views.EditJobCategory, name='editjobcategory'),
    path('updatejobcategory/<int:id>/', views.updatejobcategory, name='updatejobcategory'),
    path('deletejobcategory/<int:id>/', views.DeleteJobCategory, name='deletejobcategory'),

    path('addjob/', views.AddJob, name='addjob'),
    path('savejob/', views.savejob, name='savejob'),
    path('displayjob/', views.DisplayJob, name='displayjob'),
    path('editjob/<int:id>/', views.EditJob, name='editjob'),
    path('updatejob/<int:id>/', views.UpdateJob, name='updatejob'),
    path('deletejob/<int:id>/', views.DeleteJob, name='deletejob'),

    path('DisplayApplications/', views.DisplayApplications, name='DisplayApplications'),
    path('deleteapplication/<int:id>', views.DeleteApplication, name='deleteapplication'),
    path('applicantprofile/<name>/',views.GetApplicantD,name='applicantprofile'),
    path('displaymsg',views.DisplayMessages,name='displaymsg')

]