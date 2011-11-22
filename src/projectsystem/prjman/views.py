# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from projectsystem.prjman.models import ProjectForm, Project

def addprj(request):
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            pass
    else:
        form=ProjectForm()   
    return render_to_response('projectadd.html', {
        'form': form,
    }) 
    
def listprj(request):
    project_list=Project.objects.all();
    return render_to_response('projectlist.html',{'project_list':project_list});    

def site_home(request):
    return render_to_response('index.html');    

def project_detail(request,project_id):
    print project_id
    project_list=Project.objects.all();
    return render_to_response('projectlist.html',{'project_list':project_list});    

def project_add(request):
    project_list=Project.objects.all();
    return render_to_response('projectlist.html',{'project_list':project_list});    

def project_del(request):
    project_list=Project.objects.all();
    return render_to_response('projectlist.html',{'project_list':project_list});    

def project_update(request):
    project_list=Project.objects.all();
    return render_to_response('projectlist.html',{'project_list':project_list});    