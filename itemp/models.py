from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,default='user')
    status=models.IntegerField(default=0,blank=True)
    
class Department(models.Model):
    department=models.CharField(max_length=100,null=True)
    
class Course(models.Model):
    course=models.CharField(max_length=100,null=True)
    
class Project(models.Model):
    title=models.CharField(max_length=100,null=True)
    client=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=255,null=True)
    requirements=models.CharField(max_length=255,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    document=models.FileField(upload_to="pdfs/",null=True)
    teamlead=models.CharField(max_length=255,null=True)
    status=models.IntegerField(default=0,blank=True)
    
class Developer(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    number=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    dob=models.DateField(null=True)
    address1=models.CharField(max_length=255,null=True)
    address2=models.CharField(max_length=255,null=True)
    address3=models.CharField(max_length=255,null=True)
    pincode=models.IntegerField(null=True)
    password=models.CharField(max_length=50,null=True)
    attachment=models.FileField(null=True)
    image=models.ImageField(upload_to="image/",null=True)
    status=models.IntegerField(default=0)
    
class Teamlead(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    number=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    dob=models.DateField(null=True)
    address1=models.CharField(max_length=255,null=True)
    address2=models.CharField(max_length=255,null=True)
    address3=models.CharField(max_length=255,null=True)
    pincode=models.IntegerField(null=True)
    password=models.CharField(max_length=50,null=True)
    attachment=models.FileField(null=True)
    image=models.ImageField(upload_to="image/",null=True)
    status=models.IntegerField(default=0)
    
class DailyProgress(models.Model):
    project=models.CharField(max_length=255,null=True)
    tlname=models.CharField(max_length=255,null=True)
    date=models.DateField(null=True)
    progress=models.CharField(max_length=255,null=True)
    remarks=models.CharField(max_length=255,null=True)


class Module(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    module=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=255,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    document=models.FileField(upload_to="pdfs/",null=True)
    developer=models.CharField(max_length=255,null=True)
    file=models.FileField(upload_to="pdfs/",null=True)
    status=models.IntegerField(default=0)
    
class ModuleProgress(models.Model):
    module=models.ForeignKey(Module,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    progress=models.CharField(max_length=255,null=True)
    remarks=models.CharField(max_length=255,null=True)
    
class Otp(models.Model):
    
    email=models.EmailField(null=True)
    otp=models.CharField(max_length=255,null=True)
    
    
class ProjectProgress(models.Model):
    project=models.CharField(max_length=255,null=True)
    tlname=models.CharField(max_length=255,null=True)
    date=models.DateField(null=True)
    file=models.FileField(upload_to="pdfs/",null=True)
    remarks=models.CharField(max_length=255,null=True)
    status=models.IntegerField(default=0)
    
    
class MProgress(models.Model):
    project=models.CharField(max_length=255,null=True)
    module=models.CharField(max_length=255,null=True)
    devname=models.CharField(max_length=255,null=True)
    date=models.DateField(null=True)
    file=models.FileField(upload_to="pdfs/",null=True)
    remarks=models.CharField(max_length=255,null=True)
    status=models.IntegerField(default=0)