from django.db import models
from django.forms import ModelForm



# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=140)
    manager = models.CharField(max_length=40)    
    begindate = models.DateField();
    enddate = models.DateField();

class ProjectForm(ModelForm):
    class Meta:
            model=Project
        
    
class Member(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    project = models.ManyToManyField(Project)
    
    
class Report(models.Model):
    name = models.CharField(max_length=40)
    begindate =models.DateField()
    enddate =models.DateField()
    reporter = models.ForeignKey(Member)
    
    
class ReportItem(models.Model):
    title=models.CharField(max_length=127)
    desc=models.CharField(max_length=512)
    project=models.ForeignKey(Project)
    report=models.ForeignKey(Report)
        