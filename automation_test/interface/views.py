from django.shortcuts import render
from django.http import request
from django.http import HttpResponse,HttpResponseRedirect
from interface.models import Projects
from interface.models import project_module
from interface.models import interface_cases
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404
from django import forms
# Create your views here.

def index(request):
    project=Projects.objects.all().order_by("project_id")
    return render(request, "interface/home.html",context={'home':True, 'Projects':project,'title':'接口测试'})

def backhome(request):
    return HttpResponseRedirect('/')

def backproj(request, pj_id):
    return HttpResponseRedirect('/module/'+pj_id)

def error(request):
    return render(request, "interface/errors.html")

# class index(ListView):
#     model=Projects
#     title= '接口测试'
#     context_object_name='Projects'
#     template_name = 'interface/home.html'
#     paginate_by = 8



#
# class modules(ListView):
#     model=interface_cases
#     template_name = 'interface/home.html'
#     context_object_name="m_list"
#     #context_module_name="m_list"



def modules(request,pj_id):
    try:
        project = Projects.objects.all().order_by("project_id")
        project_name=Projects.objects.get(project_id=pj_id)
        model_list=project_module.objects.filter(project_id=pj_id)
    except:
        return HttpResponseRedirect('/error/')
    else:
        return render(request, "interface/tables.html",context={'Projects':project, 'project_name':project_name,'project_id':pj_id,'title':'测试模块', 'm_list': model_list})

def delete(request,pj_id):
    module_name = request.POST.get("check_box_list")
    try:
        project_name = project_module.objects.get(module_name=module_name)
    except:
        return HttpResponseRedirect('/error/')
    else:
        if request.method == "POST":
            check_box_list = request.POST.getlist('check_box_list')
            if check_box_list:
                for i in check_box_list:
                    project_module.objects.filter(module_name=i).delete()
            else:
                return HttpResponseRedirect('/module/' + str(project_name.project_name_id))
            return HttpResponseRedirect('/module/' + str(project_name.project_name_id))
        else:
            return HttpResponse("未知错误")

def module_create(request,pj_id):
    try:
        project_name = Projects.objects.get(id=pj_id)
    except:
        return HttpResponseRedirect('/error/')
    else:
        return render(request, "interface/new_module.html", context={'title':'新建模块','project_name':project_name })

def module_commit(request,pj_id):

    if request.method == 'POST':
        module_name=request.POST.get("module_name")
        project_name=request.POST.get("project_name")
        try:
          project_id = Projects.objects.get(project_name=project_name)
          project_module.objects.create(module_name=module_name, project_name_id=project_id.id)
        except:
            return HttpResponseRedirect('/error/')
        else:
            return HttpResponseRedirect('/module/'+str(project_id.id))

    else:
        return HttpResponseRedirect('/error/')

def module_cases(request, pj_id, mod_name):
    try:
        module_selected = project_module.objects.get(project_name_id=pj_id,module_name=mod_name)
        project_name = Projects.objects.get(id=pj_id)
        testcases = interface_cases.objects.filter(project_id=pj_id, module_id=module_selected.id).order_by('test_id')
    except:
        return HttpResponseRedirect('/error/')
    else:
        if testcases:
            return render(request, "interface/cases.html", context={'project_name':project_name,'module_name':mod_name,'title':'模块用例','testcases':testcases})
        else:
            return render(request, "interface/cases.html", context={'project_name':project_name,'module_name':mod_name, 'title':'模块用例'})





