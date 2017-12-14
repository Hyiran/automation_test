from django.db import models
from django.urls import reverse

# Create your models here.
class user(models.Model):
    ID=models.IntegerField
    name=models.CharField(max_length=10)

    def  __str__(self):
        return self.name

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=20)
    project_status = models.IntegerField()
    project_createtime = models.DateTimeField(auto_now_add=True,)
    project_updatetime = models.DateTimeField(auto_now=True,null=True )
    project_creator = models.CharField(max_length=20)
    project_updator = models.CharField(max_length=20,null=True)
    project_comments = models.TextField()

    def  __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse('project:table', kwargs={'pk': self.pk})

class project_module(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=20)
    project_id = models.IntegerField()
    module_createtime = models.DateTimeField(auto_now_add=True)
    module_updatetime = models.DateTimeField(auto_now=True,null=True)
    module_creator = models.CharField(max_length=20)
    module_updator = models.CharField(max_length=20, null=True)
    modulecomments = models.TextField()

class testcase_module(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=20)
    project_id = models.IntegerField()
    module_createtime = models.DateTimeField(auto_now_add=True)
    module_updatetime = models.DateTimeField(auto_now=True)
    module_creator = models.CharField(max_length=20)
    module_updator = models.CharField(max_length=20)
    comments = models.TextField()

class interfaces(models.Model):
    interface_id=models.AutoField(primary_key=True)
    interface_host=models.CharField(max_length=20, null=True)
    interface_url=models.CharField(max_length=20, null=True)
    module_id = models.IntegerField()
    project_id = models.IntegerField()

class testcases(models.Model):
    test_id = models.CharField(max_length=20)
    topic = models.TextField()
    steps = models.TextField()
    expected = models.TextField()
    obtained = models.TextField()
    module_id=models.IntegerField()
    type=models.CharField(max_length=1)
    status=models.IntegerField()
    testcases_createtime = models.DateTimeField(auto_now_add=True)
    testcases_updatetime = models.DateTimeField(auto_now=True)
    testcases_creator = models.CharField(max_length=20)
    testcases_updator = models.CharField(max_length=20)
    comments = models.TextField()

class interface_cases(models.Model):
    case_id = models.CharField(max_length=20)
    test_id = models.CharField(max_length=20)
    mathod=models.CharField(max_length=10)
    interface_id=models.IntegerField()
    module_id = models.IntegerField()
    project_id = models.IntegerField()
    head=models.TextField()
    data=models.TextField()
    token=models.CharField(max_length=255)
    status=models.IntegerField()
    testcases_createtime = models.DateTimeField(auto_now_add=True)
    testcases_updatetime = models.DateTimeField(auto_now=True,null=True)
    testcases_creator = models.CharField(max_length=20)
    testcases_updator = models.CharField(max_length=20,null=True)
    comments = models.TextField()


class test_results(models.Model):
    result_id=models.CharField(max_length=255)
    job_id=models.CharField(max_length=255)
    interfacecase_id=models.CharField(max_length=255)
    return_code=models.IntegerField()
    expected_contents=models.TextField()
    obtained_contents=models.TextField()
    module_id=models.IntegerField()
    project_id=models.IntegerField()
    status=models.IntegerField()
    runtime=models.DateTimeField(auto_now_add=True)

class test_tasks(models.Model):
    task_id = models.CharField(max_length=255)
    case_id = models.CharField(max_length=255)
    status = models.IntegerField()
    begintime=models.DateTimeField()
    endtime=models.DateTimeField()
    tasks_creator = models.CharField(max_length=20)


class monitor_tasks(models.Model):
    task_id = models.CharField(max_length=255)
    case_id = models.CharField(max_length=255)
    status = models.IntegerField()
    begintime=models.DateTimeField()
    cycle=models.IntegerField()
    warning_event=models.BooleanField()
    tasks_creator = models.CharField(max_length=20)


class monitor_results(models.Model):
    task_id = models.CharField(max_length=255)
    case_id = models.CharField(max_length=255)
    return_code=models.IntegerField()
    expected_contents=models.TextField()
    obtained_contents=models.TextField()
    status = models.IntegerField()
    runtime=models.DateTimeField(auto_now_add=True)

