"""Interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  interface import views


urlpatterns = [

    #url(r'^$', views.index.as_view()),
    url(r'^$', views.index),
    url(r'^.*backhome$', views.backhome),
    url(r'^.*/(?P<pj_id>\d+)/backproj$', views.backproj),
    url(r'^.*/(?P<pj_id>\d+)/module_new/backproj$', views.backproj),
    url(r'^error/$', views.error,name="error_page"),
    url(r'^module/(?P<pj_id>\d+)/$', views.modules, name = 'modules'),
    url(r'^module/(?P<pj_id>\d+)/module=(?P<mod_name>.*)$', views.module_cases, name = 'module_cases'),
    url(r'^module/(?P<pj_id>\d+)/module_delete/$', views.delete, name = 'module_delete'),
    url(r'^module/(?P<pj_id>\d+)/module_new/$', views.module_create, name = 'module_create'),
    url(r'^module/(?P<pj_id>\d+)/module_new/commit/$', views.module_commit, name = 'module_edit'),
    url(r'^admin/', admin.site.urls),
]
