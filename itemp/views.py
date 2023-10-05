from datetime import datetime
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from .models import *
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .DB import DbConnection
from django.contrib.auth import logout
import os
from django.contrib.auth.decorators import login_required


dbobj=DbConnection(host="localhost",user="root",passwd="",database="itemployee",port=3306)
def loginaction(request):
    username=request.POST["username"]
    password=request.POST["password"]
    record=UserAccount.objects.filter(username=username,password=password,status=1)
    if record.count()>0:
        record=UserAccount.objects.get(username=username,password=password)
        
        request.session['role']=record.role
        if record.role=="admin":
            return redirect('admin_home')
        elif record.role=='tl':
            request.session['tusername'] = record.username
            user=Teamlead.objects.get(username=request.session['tusername'])
            pro=Project.objects.filter(teamlead=user.name,status=0).count()
            user.count=pro
            return render(request,"tl_home.html",{'user':user})
        else:
            request.session['dusername'] = record.username
            user=Developer.objects.get(username=request.session['dusername'])
            count=0
    
            count=Module.objects.filter(developer=user.name,status=0).count()
            return render(request,"dev_home.html",{'user':user,'count':count})
        
    else:
        return render(request,'login.html',{'errmsg':'Invlid username or password, or your account is not activated'})
    
# Create your views here.
def generate_random_password(length=10):
    return ''.join(random.choice(string.digits) for _ in range(6))
generated_password = generate_random_password()
def custom_logout(request):
    logout(request)
    return redirect('login')
def nav(request):
    return render(request,'nav.html')

def index(request):
    return render(request,'index.html')


def admin_home(request):
    count1=Project.objects.filter(status=0).count()
    return render(request,'adminhome.html',{'count1':count1})

def tl_home(request):
    # current_user= request.teamlead.id
    # user1=Teamlead.objects.get(id=current_user)
    user=Teamlead.objects.get(username=request.session['tusername'])
    pro=Project.objects.filter(teamlead=user.name,status=0).count()
    user.count=pro
    return render(request,"tl_home.html",{'user':user})



def dev_home(request):
    # current_user= request.teamlead.id
    # user1=Teamlead.objects.get(id=current_user)
    user=Developer.objects.get(username=request.session['dusername'])
    count=0
    
    count=Module.objects.filter(developer=user.name,status=0).count()
    
    
    
    return render(request,"dev_home.html",{'user':user,'count':count})

def tl_profile(request):
    # current_user= request.teamlead.id
    # user1=Teamlead.objects.get(id=current_user)
    user=Teamlead.objects.get(username=request.session['tusername'])
    return render(request,"tl_profile.html",{'user':user})

def dev_profile(request):
    # current_user= request.teamlead.id
    # user1=Teamlead.objects.get(id=current_user)
    user=Developer.objects.get(username=request.session['dusername'])
    return render(request,"dev_profile.html",{'user':user})

def tl_signup(request):
    course=Course.objects.all()
    department=Department.objects.all()
    return render(request,'tl_signup.html',{'course':course,'department':department})

def dev_signup(request):
    course=Course.objects.all()
    department=Department.objects.all()
    return render(request,'dev_signup.html',{'course':course,'department':department})

def login(request):
    return render(request,'login.html')

#-------------------------------------------------------------------------------promote user

def promoteuser(request):
    use=UserAccount.objects.filter(status=1)
    user=Teamlead.objects.filter(status=1)
    user1=Developer.objects.filter(status=1)
    return render(request,'promoteuser.html',{'user':user,'user1':user1,'use':use})

def promouser(request,username):
    dev=Developer.objects.get(username=username)
    tl=Teamlead.objects.create(name=dev.name,username=username,number=dev.number,email=dev.email,dob=dev.dob,address1=dev.address1,address2=dev.address2,address3=dev.address3,pincode=dev.pincode,password=dev.password,attachment=dev.attachment,status=dev.status,course_id=dev.course_id,department_id=dev.department_id,image=dev.image)
    tl.save()
    user=UserAccount.objects.get(username=username)
    user.role="tl"
    user.save()
    dev.delete()
    subject="Employee Portal"
    message=" Dear {name},  \n\n You are Promoted as Team Lead. \n\n Thank You.".format(name=dev.name,)
    send_mail(subject,message,settings.EMAIL_HOST_USER,[dev.email])
    print(message) 
    return redirect(promoteuser)
    return redirect(promoteuser)

def depromouser(request,username):
    tl=Teamlead.objects.get(username=username)
    dev=Developer.objects.create(name=tl.name,username=username,number=tl.number,email=tl.email,dob=tl.dob,address1=tl.address1,address2=tl.address2,address3=tl.address3,pincode=tl.pincode,password=tl.password,attachment=tl.attachment,status=tl.status,course_id=tl.course_id,department_id=tl.department_id,image=tl.image)
    dev.save()
    user=UserAccount.objects.get(username=username)
    user.role="developer"
    user.save()
    tl.delete()
    subject="Employee Portal"
    message=" Dear {name}, \n\n Welcome to Employee Portal. \n\n You are Depromoted as Developer. \n\n Thank You.".format(name=tl.name)
    send_mail(subject,message,settings.EMAIL_HOST_USER,[tl.email])
    print(message) 
    return redirect(promoteuser)
    
#------------------------------------------------------------------------------adding users
def adduser(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        address1=request.POST['address1']
        address2=request.POST['address2']
        address3=request.POST['address3']
        number=request.POST['number']
        dob=request.POST['dob']
        pincode=request.POST['pincode']
        password=generated_password
        file=request.FILES.get('file')
        img=request.FILES.get('img')
        sel=request.POST['sel']
        sel1=request.POST['sel1']
        role=request.POST['role']
        department1=Department.objects.get(id=sel1)
        course1=Course.objects.get(id=sel)
        user=UserAccount.objects.create(username=username,password=generated_password,role=role)

        if role == "tl":
            tl=Teamlead.object.create(username=username,name=name,address1=address1,address2=address2,address3=address3,number=number,email=email,dob=dob,pincode=pincode,attachment=file,course=course1,department=department1,password=generated_password,image=img)
        else:
            dev=Developer.objects(username=username,name=name,address1=address1,address2=address2,address3=address3,number=number,email=email,dob=dob,pincode=pincode,attachment=file,course=course1,department=department1,password=generated_password,image=img)
         
        dev.save()
        user.save()
        subject="Registration Successfull"
        message=" Dear {name}, \n\n Welcome to Employee Portal. \n\n Your Login Credentials are, \n User name : {username} \n Password   : {password} \n\n Thank You.".format(name=name,username=username,password=password)
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
        print(message) 
        return redirect(manage_users)
    else:
        course=Course.objects.all()
        department=Department.objects.all()
        return render(request,'adduser.html',{'course':course,'department':department})
#-----------------------------------------------------------------------------deleting users
def deleteuser(request):
    user=UserAccount.objects.filter(status=1).exclude(role="admin")
    
    
    return render(request,'deleteuser.html',{'user':user})
def deluser(request,username,role):
    user=UserAccount.objects.get(username=username)
    user.delete()
    if role=="tl":
        user=Teamlead.objects.get(username=username)
        user.delete()
    else:
        user=Developer.objects.get(username=username)
        user.delete()
        
    return redirect(deleteuser)

def adddep(request):
    if request.method=='POST':
        department=request.POST['department']
        dep=Department(department=department)
        dep.save()
    return render(request,"adddepartment.html")

def addcourse(request):
    if request.method=='POST':
        course=request.POST['course']
        course1=Course(course=course)
        course1.save()
    return render(request,"addcourse.html")

def projectpublish(request):
    return render(request,'addproject.html')

def addproject(request):
    if request.method=='POST':
        title=request.POST['title']
        client=request.POST['client']
        description=request.POST['description']
        req=request.POST['req']
        stdate=request.POST['stdate']
        endate=request.POST['endate']
        doc=request.FILES.get('doc')

    project=Project(title=title,client=client,description=description,requirements=req,start_date=stdate,end_date=endate,document=doc) 
    project.save()

    return redirect('projectpublish')

def devsignupaction(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        address1=request.POST['address1']
        address2=request.POST['address2']
        address3=request.POST['address3']
        number=request.POST['number']
        dob=request.POST['dob']
        pincode=request.POST['pincode']
        password=generated_password
        file=request.FILES.get('file')
        img=request.FILES.get('img')
        sel=request.POST['sel']
        sel1=request.POST['sel1']
        
        role='developer'
        var=Teamlead.objects.filter(email=email).count()
        print(var)
       
        if var>0:
            errmsg='This Email is Already Registered'
            return render(request,'tl_signup.html',{'errmsg':errmsg})
        else:
            department1=Department.objects.get(id=sel1)
            course1=Course.objects.get(id=sel)
            dev=Developer.objects.create(username=username,name=name,address1=address1,address2=address2,address3=address3,number=number,email=email,dob=dob,pincode=pincode,attachment=file,course=course1,department=department1,password=password,image=img)
            useraccount=UserAccount.objects.create(username=username,password=generated_password,role=role)

            dev.save()
            useraccount.save()
            subject="Registration Successfull"
            message=" Dear {name}, \n\n Welcome to Employee Portal. \n\n Your Login Credentials are, \n User name : {username} \n Password   : {password} \n\n Thank You.".format(name=name,username=username,password=password)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
            print(message)
            return redirect(login)
            return redirect('/')
            return redirect(login)
    
def tlsignupaction(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        address1=request.POST['address1']
        address2=request.POST['address2']
        address3=request.POST['address3']
        number=request.POST['number']
        dob=request.POST['dob']
        pincode=request.POST['pincode']
        password=generated_password
        file=request.FILES.get('file')
        img=request.FILES.get('img')
        sel=request.POST['sel']
        sel1=request.POST['sel1']
        
        role='tl'
        var=Teamlead.objects.filter(email=email).count()
        print(var)
       
        if var>0:
            errmsg='This Email is Already Registered'
            return render(request,'tl_signup.html',{'errmsg':errmsg})
        else:
           
            department1=Department.objects.get(id=sel1)
            course1=Course.objects.get(id=sel)
            tl=Teamlead.objects.create(username=username,name=name,address1=address1,address2=address2,address3=address3,number=number,email=email,dob=dob,pincode=pincode,attachment=file,course=course1,department=department1,password=password,image=img)
            useraccount=UserAccount.objects.create(username=username,password=generated_password,role=role)
        
            tl.save()
            useraccount.save()
            subject="Registration Successfull"
            message=" Dear {name}, \n\n Welcome to Employee Portal. \n\n Your Login Credentials are, \n User name : {username} \n Password   : {password} \n\n Thank You.".format(name=name,username=username,password=password)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
            print(message)
            return redirect(login)
    

def validatedev(request):
    dev=Developer.objects.filter(status=0)
    return render(request,'approvedev.html',{'dev':dev})

def approvedev(request,username):
    account=UserAccount.objects.get(username=username)
    account.status=1
    account1=Developer.objects.get(username=username)
    account1.status=1
    account1.save()
    account.save()
    return redirect('validatedev')
    
def validatetl(request):
    tl=Teamlead.objects.filter(status=0)
    return render(request,'approvetl.html',{'tl':tl})

def approvetl(request,username):
    account=UserAccount.objects.get(username=username)
    account.status=1
    account1=Teamlead.objects.get(username=username)
    account1.status=1
    account1.save()
    account.save()
    return redirect('validatetl')
# def register_developer(name, email, password):
#     if is_password_complex(password):
#         # Create the DeveloperRegistration instance and proceed
#     else:
#         # Password doesn't meet complexity requirements, handle accordingly
def reject(request,username):
    user=UserAccount.objects.get(username=username)
    user.delete()
    tl=Teamlead.objects.get(username=username)
    tl.delete()
    return redirect(validatetl)

def reject_dev(request,username):
    print(username)
    user=UserAccount.objects.get(username=username)
    user.delete()
    dev=Developer.objects.get(username=username)
    dev.delete()
    return redirect(validatedev)
    
def is_password_complex(password):
    # Check if the password contains at least one letter and one digit
    return any(c.isalpha() for c in password) and any(c.isdigit() for c in password)

def changepassword_dev(request):
    return render(request,'dev_changepassword.html')

def updatepassword_dev(request):
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    username=request.session['dusername']
    sql="select password from itemp_useraccount where username=%s"
    val=(username,)
    p=getstring(sql,val)
    if p==password:
        if is_password_complex(password):
            if newpassword==confirmpassword:
                sql="update itemp_useraccount set password=%s where username=%s"
                val=(newpassword,username)
                if dbobj.executenonquery(sql,val):
                    errmsg='Password changed successfully'
                    return render(request,'dev_changepassword.html',{'errmsg':errmsg})
                else:
                    errmsg='Unable to change password at this time'
                    return render(request,'dev_changepassword.html',{'errmsg':errmsg})
            else:
                errmsg='New Password and Confirm Password must be the same'
                return render(request,'dev_changepassword.html',{'errmsg':errmsg})
        else:
            errmsg='Password Must Conatin A Special Charecter'
            return render(request,'dev_changepassword.html',{'errmsg':errmsg})
    else:
        errmsg='Invalid Current Password'
        return render(request,'dev_changepassword.html',{'errmsg':errmsg})

def changepassword(request):
    return render(request,'tl_changepassword.html')

def updatepassword(request):
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    username=request.session['tusername']
    sql="select password from itemp_useraccount where username=%s"
    val=(username,)
    p=getstring(sql,val)
    if p==password:
        if is_password_complex(password):
            if newpassword==confirmpassword:
                sql="update itemp_useraccount set password=%s where username=%s"
                val=(newpassword,username)
                if dbobj.executenonquery(sql,val):
                    errmsg='Password changed successfully'
                    return render(request,'tl_changepassword.html',{'errmsg':errmsg})
                else:
                    errmsg='Unable to change password at this time'
                    return render(request,'tl_changepassword.html',{'errmsg':errmsg})
            else:
                errmsg='New Password and Confirm Password must be the same'
                return render(request,'tl_changepassword.html',{'errmsg':errmsg})
        else:
            errmsg='Password Must Conatin A Special Charecter'
            return render(request,'tl_changepassword.html',{'errmsg':errmsg})
    else:
        errmsg='Invalid Current Password'
        return render(request,'tl_changepassword.html',{'errmsg':errmsg})
    

def getstring(sql,val):
    d=dbobj.selectrecords(sql,val)
    print(sql)
    s=""
    for row in d:
        s=row[0]
    print("password:"+str(s))
    return s

def assignview(request):
    if request.method=="POST":
        tlid=request.POST['tlname']
        projectid=request.POST['projectname']
        
        tl=Teamlead.objects.get(id=tlid)
        project=Project.objects.get(id=projectid)
        project.teamlead=tl.name
        project.save()
        progress=DailyProgress.objects.create(project=project.title,tlname=tl.name,date=datetime.now().date(),progress="NOT Started Yet",remarks="Null")
        progress.save()
        var3=Project.objects.all().values_list('teamlead')
        var1=Teamlead.objects.exclude(name__in=var3).filter(status=1)
        var=Project.objects.filter(teamlead__isnull=True)
        return render(request,'assign_project.html',{'var':var,'var1':var1})
    else:
        
        var3=Project.objects.filter(teamlead__isnull=False).values_list('teamlead')
        var1=Teamlead.objects.exclude(name__in=var3).filter(status=1)
        var=Project.objects.filter(teamlead__isnull=True)
        return render(request,'assign_project.html',{'var':var,'var1':var1})
    
def assignedtlview(request):
    user=Teamlead.objects.get(username=request.session['tusername'])
    pro=Project.objects.filter(teamlead=user.name)
    for p in pro:
        
        c=ProjectProgress.objects.filter(project=p.title,status=1).count()
        if p.status==1:
            p.count=100
        else:
            c=c*20
            p.count=c
    return render(request,'tl_assigned.html',{'pro':pro})

# def progress(request):
#     pro=DailyProgress.objects.all()
#     progress_percentage = 100  # For example, 50% progress

    
#     return render(request,'dailyprogress.html',{'pro':pro,'progress_percentage': progress_percentage})

def tl_project_list(request):
    user=Teamlead.objects.get(username=request.session['tusername'])
    pro=Project.objects.filter(teamlead=user.name)
    return render(request,'tl_project_list.html',{'pro':pro})

def progress1(request):
    pro=ModuleProgress.objects.all()
    user=Teamlead.objects.get(username=request.session['tusername'])
    project=Project.objects.filter(teamlead=user.name).values_list('id')
    
    pro=Module.objects.filter(project_id__in=project)
    for p in pro:
        
        c=MProgress.objects.filter(module=p.module,status=1).count()
        if p.status==1:
            c=100
            p.count=c
        else:
            c=c*20
            p.count=c
    # pro=Project.objects.all()
    # for p in pro:
    #     mod=Module.objects.get(id=p.module_id)
    #     p.moduletitle=mod.module
    return render(request,'progress.html',{'pro':pro})

def progress2(request):
    pro=ModuleProgress.objects.all()
    user=Developer.objects.get(username=request.session['dusername'])
    project=Project.objects.filter(teamlead=user.name).values_list('id')
    
    pro=Module.objects.filter(developer=user.name)
    for p in pro:
        
        c=MProgress.objects.filter(module=p.module,status=1).count()
        if p.status==1:
            c=100
            p.count=c
        else:
            c=c*20
            p.count=c
    # pro=Project.objects.all()
    # for p in pro:
    #     mod=Module.objects.get(id=p.module_id)
    #     p.moduletitle=mod.module
    return render(request,'progress_dev.html',{'pro':pro})


def devprogress(request):
    
    pro=ModuleProgress.objects.all()
    user=Teamlead.objects.get(username=request.session['tusername'])
    project=Project.objects.filter(teamlead=user.name)
    print(user.name)
    
    return render(request,'devprogress.html',{'pro':pro,'project':project})
def moduleprogress(request):
    user=Developer.objects.get(username=request.session['dusername'])
    pro=Module.objects.filter(developer=user.name)
    
    
    return render(request,'moduleprogress.html',{'pro':pro})
def modulefile(request,id):
    if request.method=="POST":
        file=request.FILES.get('doc')
        pro=Module.objects.get(id=id)
        pro.file=file
        pro.save()
        modp=ModuleProgress.objects.get(module_id=id)
        modp.progress="Completed"
        modp.save()
        return redirect(moduleprogress)
    else:
        pro=Module.objects.get(id=id)
        
        return render(request,'modulefile.html',{'pro':pro})
def progressupdate(request,title):
    if request.method=="POST":
        progress=request.POST['progress']
        remarks=request.POST['remarks']
        pro=DailyProgress.objects.get(project=title)
        if pro.progress == "NOT Started Yet":
        
            pro.progress=progress
            pro.remarks=remarks
            pro.save()
        else:
            DailyProgress.objects.create(project=pro.project,tlname=pro.tlname,date=datetime.now().date(),progress=progress,remarks=remarks)
        user=Teamlead.objects.get(username=request.session['tusername'])
        pro=Project.objects.filter(teamlead=user.name)
        return render(request,'tl_assigned.html',{'pro':pro})
    else:
        pro=Project.objects.get(title=title)
        
        date=datetime.now().date()
        return render(request,'progressupdate.html',{'pro':pro,'date':date})

from django.shortcuts import get_list_or_404
from mimetypes import guess_type
def download_pdf(request, pdf_id):
    project = get_object_or_404(Project, pk=pdf_id)
    

    if project.document:  # Check if a document is attached
        response = FileResponse(project.document, as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{project.document.name}"'
        return response
    else:
        raise Http404("The project doesn")
    
def download_pdf2(request, pdf_id):
    project = get_object_or_404(Module, pk=pdf_id)
    

    if project.document:  # Check if a document is attached
        response = FileResponse(project.document, as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{project.document.name}"'
        return response
    else:
        raise Http404("The project doesn")

def download_pdf3(request, pdf_id):
    project = get_object_or_404(MProgress, pk=pdf_id)
    

    if project.file:  # Check if a document is attached
        response = FileResponse(project.file, as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{project.file.name}"'
        return response
    else:
        raise Http404("The project doesn")


def download_pdf1(request, pdf_id):
    project = get_object_or_404(Module, pk=pdf_id)
    

    if project.document:  # Check if a document is attached
        response = FileResponse(project.document, as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{project.document.name}"'
        return response
    else:
        raise Http404("The project doesn")

# def download_pdf1(request, pdf_id):
#     project = get_object_or_404(Module, pk=pdf_id)
    

#     if project.document:  # Check if a document is attached
#         response = FileResponse(project.document, as_attachment=True)
#         response['Content-Disposition'] = f'attachment; filename="{project.document.name}"'
#         return response
#     else:
#         raise Http404("The project doesn")

from django.db.models.signals import post_save
from django.dispatch import receiver

def progress_view(request):
    # Calculate progress (0 to 100)
    progress_percentage = 50  # For example, 50% progress

    context = {'progress_percentage': progress_percentage}
    return render(request, 'progress_template.html',context)


def tlprojects(request):
    return render(request,'tl_project.html')

def manage_users(request):
    return render(request,'manageusers.html')

def editprofile(request):
    username=request.session['username']
    login = UserAccount.objects.get(username=username)
    return render(request,'editprofile.html', {'login':login})


    
def assignmodule(request):
    if request.method=="POST":
        dev=request.POST['devname']
        projectid=request.POST['projectname']
        module=request.POST['module']
        stdate=request.POST['stdate']
        enddate=request.POST['enddate']
        doc=request.FILES.get('doc')
        
        mod=Module.objects.create(module=module,start_date=stdate,end_date=enddate,document=doc,developer=dev,project_id=projectid,file="NULL")
        mod.save()
        mod1=Module.objects.get(module=module)
        print(mod1.id)
        progress=ModuleProgress.objects.create(date=datetime.now().date(),progress="Pending",module_id=mod1.id)
        progress.save()
        user=Teamlead.objects.get(username=request.session['tusername'])

        var4=Project.objects.filter(teamlead=user.name)
        var3=Module.objects.all().values_list('developer')
        var1=Developer.objects.exclude(name__in=var3).filter(status=1)
        var=Module.objects.filter(developer__isnull=True)
        return render(request,'assign_module.html',{'var':var,'var1':var1,'var4':var4})
    else:
        user=Teamlead.objects.get(username=request.session['tusername'])
        
        var4=Project.objects.filter(teamlead=user.name)
        var3=Module.objects.all().filter(file__isnull=True).values_list('developer')
        print(var3)
        var1=Developer.objects.exclude(name__in=var3).filter(status=1)
        for var in var1:
            print(var.name)
        var=Module.objects.filter(developer__isnull=True)
        return render(request,'assign_module.html',{'var':var,'var1':var1,'var4':var4})

def editpage(request):
    tl=Teamlead.objects.get(username=request.session['tusername'])
    return render (request,"edit_tl.html",{'tl':tl})

def edit_tl_details(request,username):
    if request.method == "POST":
        tl=Teamlead.objects.get(username=username)
        tl1=UserAccount.objects.get(username=username)
        tl.name=request.POST['name']
        tl1.username=request.POST['username']
        tl.email=request.POST['email']
        tl.dob=request.POST['dob']
        tl.address1=request.POST['address1']
        tl.address2=request.POST['address2']
        tl.address3=request.POST['address3']
        tl.pincode=request.POST['pincode']
        tl.number=request.POST['number']
        if len(request.FILES)!=0:
            if len(tl.image)>0:
                os.remove(tl.image.path)
            tl.image = request.FILES.get('img')
        tl.save()
        tl1.save()
        
        return redirect("editpage")
    return render(request,"edit_tl.html")

def editpage_dev(request):
    dev=Developer.objects.get(username=request.session['dusername'])
    return render (request,"edit_dev.html",{'dev':dev})

def edit_dev_details(request,username):
    if request.method == "POST":
        dev=Teamlead.objects.get(username=username)
        dev1=UserAccount.objects.get(username=username)
        dev.name=request.POST['name']
        dev1.username=request.POST['username']
        dev.email=request.POST['email']
        dev.dob=request.POST['dob']
        dev.address1=request.POST['address1']
        dev.address2=request.POST['address2']
        dev.address3=request.POST['address3']
        dev.pincode=request.POST['pincode']
        dev.number=request.POST['number']
        if len(request.FILES)!=0:
            if len(dev.image)>0:
                os.remove(dev.image.path)
            dev.image = request.FILES.get('img')
        dev.save()
        dev1.save()
        
        return redirect("editpage_dev")
    return render(request,"edit_dev.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

def password_reset_request(request):
   
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        print(username)
        print(email)
        user1 = UserAccount.objects.get(username=username)
        if user1.role=="tl":
            user = Teamlead.objects.get(username=username)
        elif user1.role=="developer":
            user = Developer.objects.get(username=username)
        email=user.email
        otp=generated_password
        if email==user.email:
            Otp.objects.create(email=email,otp=otp).save()
            subject="Reset Password"
            message=" Dear {name},otp: {otp} \n\n Thank You.".format(name=user.name,otp=otp)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email])

            # You can redirect to a success page
            return render(request, "password_reset_confirm.html",{"username":username})
        
    return render(request, "password_reset_request.html")


def password_reset_confirm(request,username):
    
    if request.method == "POST":
        otp=request.POST['otp']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        getotp=Otp.objects.get(otp=otp)
        if getotp:
            if password==cpassword:
                user1 = UserAccount.objects.get(username=username)
                if user1.role=="tl":
                    user = Teamlead.objects.get(username=username)
                    user1.password=password
                    user1.save()
                    user.password=password
                    user.save()
                    
                elif user1.role=="developer":
                    user = Developer.objects.get(username=username)
                    user1.password=password
                    user1.save()
                    user.password=password
                    user.save()
        return redirect("login")

       

    else:
        return render(request, "password_reset_confirm.html")



#--------------------------------------------------------------------------------------progesss
def adminprogress(request):
    pro=Project.objects.exclude(teamlead=None)
    progress_percentage = 100  # For example, 50% progress
    for i in pro:
        pro1=DailyProgress.objects.get(project=i.title)
        i.progress=pro1.progress
        
    
    return render(request,'adminp.html',{'pro':pro,'progress_percentage': progress_percentage})

def more(request,project):
    pro=Project.objects.get(title=project)
    for i in pro:
        pro1=DailyProgress.objects.get(project=i.title)
        i.progress=pro1.progress
        
    
    return render(request,'adminp.html',{'pro':pro})


def p_progress(request):
    user=Teamlead.objects.get(username=request.session['tusername'])
    pro=Project.objects.filter(teamlead=user.name)
    if request.method == "POST":
        ProjectProgress.objects.create(project=request.POST['project'],tlname=user.name,date=datetime.now().date(),file=request.FILES.get('doc'),remarks=request.POST['remarks']).save()
    
    
    
    return render(request,'projectprogress.html',{'pro':pro})

def verify(request,id):
    
    pro=ProjectProgress.objects.get(id=id)
    
    pro.status=1
    pro.save()
    return redirect(projectprogress)

def verify1(request,id):
    
    pro=Project.objects.get(id=id)
    
    pro.status=1
    pro.save()
    return redirect(moredetails)

def projectprogress(request):
    
    pro=ProjectProgress.objects.all()
    
    return render(request,'adminprojectprogress.html',{'pro':pro})
def moredetails(request,id):
    
    pro1=Project.objects.get(id=id)
    
    pro=ProjectProgress.objects.filter(project=pro1.title)
    c=pro.count()
    flag=pro1.title
    return render(request,'more.html',{'pro':pro,'flag':flag,'c':c})

def mark_completed(request,project):
    
    pro1=Project.objects.get(title=project)
    pro1.status=1
    pro1.save()
    
    return redirect(progress)

def download_pdf2(request, pdf_id):
    project = get_object_or_404(ProjectProgress, pk=pdf_id)
    

    if project.document:  # Check if a document is attached
        response = FileResponse(project.document, as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{project.document.name}"'
        return response
    else:
        raise Http404("The project doesn")

def progress(request):
    pro=Project.objects.all()
    for p in pro:
        
        c=ProjectProgress.objects.filter(project=p.title,status=1).count()
        if p.status==1:
            c=100
            p.count=c
        else:
            c=c*20
            p.count=c
    return render(request,'dailyprogress.html',{'pro':pro})


#----------------------------------------------------------------------------------------------------------------------------
def mod_update(request):
    user=Developer.objects.get(username=request.session['dusername'])
    mod=Module.objects.filter(developer=user.name)
    if request.method == "POST":
        MProgress.objects.create(project=request.POST['project'],module=request.POST['module'],devname=user.name,date=datetime.now().date(),file=request.FILES.get('doc'),remarks=request.POST['remarks']).save()
    
    return render(request,'mprogressupdate.html',{'mod':mod})

def modprogress(request):
    
    pro=MProgress.objects.all()
    
    return render(request,'devmoduleprogress.html',{'pro':pro})

def moredetails1(request,id):
    
    mod=Module.objects.get(id=id)
    
    pro=MProgress.objects.filter(module=mod.module)
    c=pro.count()
    flag=mod.module
    return render(request,'more1.html',{'pro':pro,'flag':flag,'c':c})

def moredetails2(request,id):
    
    mod=Module.objects.get(id=id)
    
    pro=MProgress.objects.filter(module=mod.module)
    c=pro.count()
    flag=mod.module
    return render(request,'more2.html',{'pro':pro,'flag':flag,'c':c})

def verify2(request,id):
    
    pro=MProgress.objects.get(id=id)
    
    pro.status=1
    pro.save()
    return redirect(modprogress)

def mark_completed1(request,project):
    
    pro1=Module.objects.get(module=project)
    pro1.status=1
    pro1.save()
    
    return redirect(progress1)