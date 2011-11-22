'''
Created on 2011-11-22

@author: Administrator
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response
from projectsystem.prjman.models import ProjectForm, Project

def site_home(request):
    return render_to_response('index.html'); 