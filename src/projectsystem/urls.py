from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from projectsystem.prjman.views import addprj,listprj,project_detail,project_add,project_del, project_update
from projectsystem.prjman.appviews.accountview import  site_home;
from projectsystem import prjman
admin.autodiscover()


urlpatterns_prj = patterns('projectsystem.prjman.views',
    url(r'^$', 'site_home'),
    url(r'^projects/$', 'listprj'),
    url(r'^projects/(?P<project_id>\d+)/$', 'project_detail'),    
    url(r'^projects/add/$', 'project_add'),    
    url(r'^projects/del/(?P<job_id>\d+)/$', 'project_del'), 
    url(r'^projects/update/(?P<job_id>\d+)/$', 'project_update'),       
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectsystem.views.home', name='home'),
    # url(r'^projectsystem/', include('projectsystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myadmin/', include(prjman.admin.admin_site.urls)),
    url(r'^prj/add$', addprj),
     url(r'^account/register/$', site_home),
)+urlpatterns_prj 