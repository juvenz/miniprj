'''
Created on 2011-7-3

@author: Administrator
'''
from django.contrib import admin
from projectsystem.prjman.models import Project,Member,Report,ReportItem
from django.contrib.admin.sites import AdminSite

admin_site=AdminSite()
admin_site.register(Project)
admin_site.register(Member)
admin_site.register(Report)
admin_site.register(ReportItem)