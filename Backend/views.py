from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from Backend.models import Coursedb,Jobdb,JobCategorydb,CourseCetogorydb
from django.contrib import messages
from Frontend.models import Signupdb, Applicationdb,Messagedb


# Create your views here.

def AdminHome(request):
    return render(request,'AdminHomePage.html')

def AdminLogin(request):
    return render(request,'AdminLogin.html')
def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request,"Login Successfully")
                return redirect(Index)
            else:
                messages.error(request,"Invalid username or password")
                return redirect(AdminLogin)
        else:
            messages.error(request,"Invalid username or password ")
            return redirect(AdminLogin)


def Index(request):
    inddata=JobCategorydb.objects.all()
    coursecat=CourseCetogorydb.objects.all()
    return render(request,'Index.html',{'inddata':inddata,'coursecat':coursecat})

def AddCourseCategory(request):
    return render(request,'AddCourseCategoryPage.html')
def savecoursecategory(request):
    if request.method=="POST":
        catg=request.POST.get('category')
        des=request.POST.get('description')
        catgobj=CourseCetogorydb(Category=catg,Description=des)
        catgobj.save()
        messages.success(request, "Coursecategory saved successfully..!")

        return redirect(AddCourseCategory)

def DisplayCourseCategory(request):
    coursecat=CourseCetogorydb.objects.all()
    return render(request,'DisplayCourseCategoryPage.html', {'coursecat': coursecat})

def EditCourseCategory(request,id):
    coursecat = CourseCetogorydb.objects.get(coursecat_id=id)
    return render(request,'EditCourseCategoryPage.html',{'coursecat':coursecat})

def UpdateCoursecategory(request,id):
    if request.method=="POST":
        cate=request.POST.get('category')
        desc=request.POST.get('description')
        CourseCetogorydb.objects.filter(coursecat_id=id).update(Category=cate,Description=desc)
        messages.success(request, "Coursecategory updated successfully..!")

        return redirect(DisplayCourseCategory)

def DeleteCourseCategory(request,id):
    dt=CourseCetogorydb.objects.get(coursecat_id=id)
    dt.delete()
    return redirect(DisplayCourseCategory)

def AddCourse(request):
    cour=CourseCetogorydb.objects.all()
    return render(request,'AddCoursePage.html',{'cour':cour})
def savecourse(request):
    if request.method=="POST":
        na=request.POST.get('name')
        cat=request.POST.get('category')
        inst=request.POST.get('institution')
        con=request.POST.get('contact')
        dur=request.POST.get('duration')
        fee=request.POST.get('fee')
        des=request.POST.get('description')
        obj=Coursedb(Course=na,Category=cat,Institution=inst,Contact=con,Duration=dur,Fees=fee,Description=des)
        obj.save()
        messages.success(request, "Course added  successfully..!")

        return redirect(AddCourse)

def DisplayCourse(request):
    data=Coursedb.objects.all()
    return render(request,'DisplayCoursePage.html',{'data':data})

def EditCourse(request,id):
    cour = CourseCetogorydb.objects.all()
    data = Coursedb.objects.get(Course_id=id)
    return render(request,'EditCoursePage.html',{'data':data,'cour':cour})

def UpdateCourse(request,id):
    if request.method=="POST":
        nm=request.POST.get('name')
        ind=request.POST.get('industry')
        instn=request.POST.get('institution')
        con=request.POST.get('contact')
        durn=request.POST.get('duration')
        fees=request.POST.get('fee')
        desc=request.POST.get('description')
        Coursedb.objects.filter(Course_id=id).update(Course=nm,Category=ind,Institution=instn,Contact=con,Duration=durn,Fees=fees,Description=desc)
        messages.success(request, "Course updated successfully..!")

        return redirect(DisplayCourse)

def DeleteCourse(request,id):
    dt=Coursedb.objects.get(Course_id=id)
    dt.delete()
    messages.success(request, "course deleted successfully..!")

    return redirect(DisplayCourse)

def AddJobCategory(request):
    return render(request,'AddJobCategoryPage.html')
def savejobcategory(request):
    if request.method=="POST":
        ind=request.POST.get('industry')
        des=request.POST.get('description')
        indobj=JobCategorydb(Industry=ind,Description=des)
        indobj.save()
        messages.success(request, "Jobcategory saved successfully..!")

        return redirect(AddJobCategory)

def DisplayJobCategory(request):
    inddata=JobCategorydb.objects.all()
    return render(request,'DisplayJobCategory.html', {'inddata': inddata})

def EditJobCategory(request,id):
    inddata = JobCategorydb.objects.get(category_id=id)
    return render(request,'EditJobCategoryPage.html',{'inddata':inddata})

def updatejobcategory(request,id):
    if request.method=="POST":
        indt=request.POST.get('industry')
        desc=request.POST.get('description')
        JobCategorydb.objects.filter(category_id=id).update(Industry=indt,Description=desc)
        messages.success(request, "Jobcategory updated successfully..!")

        return redirect(DisplayJobCategory)

def DeleteJobCategory(request,id):
    dt=JobCategorydb.objects.get(category_id=id)
    dt.delete()
    messages.success(request, "Jobcategory deleted successfully..!")

    return redirect(DisplayJobCategory)

def AddJob(request):
    ind=JobCategorydb.objects.all()
    return render(request,'AddJobPage.html',{'ind':ind})



def savejob(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        ind=request.POST.get('indus')
        cny=request.POST.get('company')
        op=request.POST.get('openings')
        exp=request.POST.get('experiance')
        loc=request.POST.get('location')
        des=request.POST.get('description')
        sal=request.POST.get('salary')
        empstat=request.POST.get('empstatus')
        obj1=Jobdb(Job_Name=nm,Industry=ind,Company=cny,Openings=op,Experiance=exp,Location=loc,Description=des,Salary=sal,Employment_status=empstat)
        obj1.save()
        messages.success(request,"Job saved successfully..!")
        return redirect(AddJob)

def DisplayJob(request):
        data = Jobdb.objects.all()
        return render(request, 'DisplayJobPage.html', {'data': data})

def EditJob(request,id):
    ind=JobCategorydb.objects.all()
    data = Jobdb.objects.get(Job_id=id)
    return render(request,'EditJobPage.html',context={'data':data,'ind':ind})

def UpdateJob(request,id):
    if request.method=="POST":
        na=request.POST.get('name')
        ind=request.POST.get('indus')
        cmp=request.POST.get('company')
        opn=request.POST.get('openings')
        ex=request.POST.get('experiance')
        lctn=request.POST.get('location')
        des=request.POST.get('description')
        sal=request.POST.get('salary')
        empstat=request.POST.get('empstatus')
        Jobdb.objects.filter(Job_id=id).update(Job_Name=na,Industry=ind,Company=cmp,Openings=opn,Experiance=ex,Location=lctn,Description=des,Salary=sal,Employment_status=empstat)
        messages.success(request,"Job updated successfully..!")

        return redirect(DisplayJob)

def DeleteJob(request,id):
    dt=Jobdb.objects.get(Job_id=id)
    dt.delete()
    messages.success(request, "Job deleted successfully..!")

    return redirect(DisplayJob)

def DisplayApplications(request):
    jobapps=Applicationdb.objects.all()
    return render(request,'DisplayJobApplications.html',{'jobapps':jobapps})
def GetApplicantD(request,name):
    p=Signupdb.objects.filter(Name=name)
    return render(request,'DisplayProfile.html',{'p':p})
def DeleteApplication(request,id):
    dltapp=Applicationdb.objects.get(Aplctn_id=id)
    dltapp.delete()
    messages.success(request, "Application removed successfully..!")
    return redirect(DisplayApplications)

def DisplayMessages(request):
    msgs=Messagedb.objects.all()
    return render(request,'DisplayMessagePage.html',{'msgs':msgs})








