from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Backend.models import Jobdb, Coursedb, JobCategorydb, CourseCetogorydb
from Frontend.models import Signupdb, Applicationdb,Messagedb


# Create your views here.


def Signup(request):
    return render(request, 'SignUp.html')


def savesignup(request):
    if request.method == "POST":
        na = request.POST.get('username')
        pa = request.POST.get('password')
        eml = request.POST.get('email')
        mob = request.POST.get('mobile')
        img = request.FILES['image']
        if Signupdb.objects.filter(Name=na).exists():
            messages.error(request, 'Username already Exists')
            return redirect(Signup)
        elif Signupdb.objects.filter(Email=eml).exists():
            messages.info(request, 'Email already registered')
            return redirect(Signup)
        else:
            pro_obj = Signupdb(Name=na, Password=pa, Email=eml, Mobile=mob, Image=img)
            pro_obj.save()
            messages.success(request, "Please login with your credentials")
            return redirect(UserLogin)

def UserLogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if Signupdb.objects.filter(Name=uname, Password=pwd).exists():
            request.session['Name'] = uname
            request.session['Password'] = pwd
            return redirect(HomePage)
        else:
            return redirect(Signup)
    return redirect(Signup)


def UserProfile(request):
    cors_cat = CourseCetogorydb.objects.all()
    username = request.session.get("Name")
    user_details = Signupdb.objects.get(Name=username)
    return render(request, 'ProfilePage.html', {'user_details': user_details, 'cors_cat': cors_cat})


def UpdateProfile(request, id):
    if request.method == "POST":
        na = request.POST.get('username')
        pa = request.POST.get('password')
        eml = request.POST.get('useremail')
        mob = request.POST.get('usermobile')
        loc = request.POST.get('location')
        qual = request.POST.get('qualification')
        apply = request.POST.get('applies')
        res = request.FILES['resume']
        Signupdb.objects.filter(Signup_id=id).update(Name=na, Password=pa, Email=eml, Mobile=mob, Location=loc,
                                                     Qualification=qual, Jobapplies=apply, Resume=res)
        messages.success(request, "Profile updated")

        return redirect(UserProfile)


def UserLogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(Signup)


def HomePage(request):
    cors_cat = CourseCetogorydb.objects.all()
    Indus = JobCategorydb.objects.all()
    return render(request, 'Home.html', {'Indus': Indus, 'cors_cat': cors_cat})

def AboutPage(request):
    cors_cat = CourseCetogorydb.objects.all()
    Indus = JobCategorydb.objects.all()
    return render(request, 'About.html', {'Indus': Indus, 'cors_cat': cors_cat})


def ContactPage(request):
    cors_cat = CourseCetogorydb.objects.all()
    Indus = JobCategorydb.objects.all()
    stat = Jobdb.objects.all()
    return render(request, 'Contact.html', {'stat': stat, 'Indus': Indus, 'cors_cat': cors_cat})



def Joblist(request):
    cors_cat = CourseCetogorydb.objects.all()
    jobs = Jobdb.objects.all()
    return render(request, 'ListJobspage.html', {'jobs': jobs,'cors_cat':cors_cat})



def Jobsingle(request, jobid):
    username = request.session.get("Name")
    user_details = Signupdb.objects.get(Name=username)
    jobs = Jobdb.objects.get(Job_id=jobid)
    return render(request, 'SingleJobPage.html', {'jobs': jobs, 'user_details': user_details})


def savejobapplications(request):
   if request.method == "POST":
        nm = request.POST.get('cand_name')
        appn_id = request.POST.get('jid')
        jnm = request.POST.get('jobname')
        em = request.POST.get('email')
        ind = request.POST.get('indus')
        cny = request.POST.get('company')
        op = request.POST.get('openings')
        exp = request.POST.get('experiance')
        loc = request.POST.get('location')
        des = request.POST.get('description')
        sal = request.POST.get('salary')
        empstat = request.POST.get('empstatus')
        if Applicationdb.objects.filter(Name=nm, Japp_id=appn_id).exists():
            messages.error(request, "Already Applied")
            return redirect(HomePage)
        else:
            obj1 = Applicationdb(Name=nm, Email=em, Japp_id=appn_id, Job_Name=jnm, Industry=ind, Company=cny, Openings=op,Experiance=exp, Location=loc, Description=des, Salary=sal, Employment_status=empstat)
            obj1.save()
            messages.success(request, "Applied successfully")
            return redirect(HomePage)


def Applicant(request, a):
    a = Applicationdb.objects.filter(Signup_id=a)
    return render(request, "SingleJobPage.html", {'a': a})


# def Joblist(request,indus):
#     cors_cat = CourseCetogorydb.objects.all()
#     Indus = JobCategorydb.objects.all()
#     job=Jobdb.objects.filter(Industry=indus)
#     # job=JobCategorydb.objects.filter(Industry=indus)
#     return render(request,'JoblistPage.html',{'job':job,'cors_cat':cors_cat,'Indus':Indus})
#
# def JobSingle(request,jobid):
#     cors_cat = CourseCetogorydb.objects.all()
#     Indus = JobCategorydb.objects.all()
#     job=Jobdb.objects.all()
#     jobs=Jobdb.objects.get(Job_id=jobid)
#     return render(request,'JobsinglePage.html',{'jobs':jobs,'cors_cat':cors_cat,'Indus':Indus,'job':job})


def Courselist(request, course_cat):
    cors_cat = CourseCetogorydb.objects.all()
    Indus = JobCategorydb.objects.all()
    cor = Coursedb.objects.filter(Category=course_cat)
    return render(request, 'CourselistPage.html', {'cor': cor, 'cors_cat': cors_cat, 'Indus': Indus})


def CourseSingle(request, cid):
    cors_cat = CourseCetogorydb.objects.all()
    Indus = JobCategorydb.objects.all()
    course = Coursedb.objects.get(Course_id=cid)
    return render(request, 'CourseSinglePage.html', {'course': course, 'cors_cat': cors_cat, 'Indus': Indus})


def JobApplications(request):
    # cors_cat = CourseCetogorydb.objects.all()
    # Indus = JobCategorydb.objects.all()
    # jobapp = Jobdb.objects.filter(Job_id=jobid)
    username = request.session.get("Name")
    pers = Applicationdb.objects.filter(Name=username)
    return render(request, 'JobApplications.html', {'pers': pers})


def Jobsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']
        jobs = Jobdb.objects.filter(Job_Name__contains=searched)
        return render(request, 'SearchJoblist.html', {'searched': searched, 'jobs': jobs})
    else:
        return render(request, 'SearchJoblist.html', {})

# def ContactPage(request):
#     cors_cat = CourseCetogorydb.objects.all()
#     Indus = JobCategorydb.objects.all()
#     stat = Jobdb.objects.all()
#     return render(request, 'Contact.html', {'stat': stat, 'Indus': Indus, 'cors_cat': cors_cat})

def Contact(request):
    cors_cat = CourseCetogorydb.objects.all()
    stat = Jobdb.objects.all()
    username = request.session.get("Name")
    reviewer = Signupdb.objects.get(Name=username)
    return render(request,'Contact.html',{'reviewer':reviewer,'stat': stat,'cors_cat': cors_cat})
def savecontact(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subjt')
        msg = request.POST.get('message')
        objcon=Messagedb(Name=nm,Email=em,subject=sub,Message=msg)
        objcon.save()
        messages.success(request, "Message sent")
        return redirect(Contact)




