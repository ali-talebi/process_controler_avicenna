from django.shortcuts import render , redirect , get_object_or_404
from django.views import View 
from .models import Detail_Process , Detail_Project , Execute_Process 
from .forms import CreateProcess , CreateExecuter
# Create your views here.


class CreateProcess_View(View):
    
    def get(self,request,project_id):
        project = Detail_Project.objects.get(id=project_id)
        form = CreateProcess(initial={'name_project':project})
        return render(request, 'process_create.html', {
            'form': form,
            'project': project
        })
        
    def post(self,request,project_id):
        project = Detail_Project.objects.get(id=project_id)
        form = CreateProcess(request.POST)
        if form.is_valid():
            process  = form.save(commit=False)
            process.name_project = project 
            process.save()
            return redirect(f'/project_detail/{project_id}/', )
            
        else:
            return render(request,'process_create.html',{'form':form})
    
    
class DeleteProcess_View(View):
    
    def get(self, request, process_id):
        instance = get_object_or_404(Detail_Process, id=process_id)
        return render(request, 'process_confirm_delete.html', {'instance': instance})
        
    def post(self, request, process_id):
        instance = get_object_or_404(Detail_Process, id=process_id)
        project_id = instance.name_project.id  
        try:
            instance.delete()
            return redirect(f'/project_detail/{project_id}/')
        except:
            return redirect(f'/project_detail/{project_id}/')
            
    
class CreateExecuter_View(View):
    

    def get(self,request,project_id,process_id):
        process = Detail_Process.objects.get(id=process_id)        
        form = CreateExecuter(initial={'process_of_work':process})
        return render(request,'task_create.html',{'form':form})
    
    def post(self,request,project_id,process_id):
        process = Detail_Process.objects.get(id=process_id)
        form = CreateExecuter(request.POST)
        if form.is_valid():
            executer = form.save(commit=False)
            executer.process_of_work = process
            executer.save()
            return redirect(f'/project_detail/{project_id}/',)
        return render(request,'task_create.html',{'form':form})
    


class DeleteExecuter_View(View):

    def get(self, request, executer_id):
        instance = get_object_or_404(Execute_Process, id=executer_id)
        return render(request, 'executer_confirm_delete.html', {'instance': instance})
        
    def post(self, request, executer_id):
        instance = get_object_or_404(Execute_Process, id=executer_id)
        project_id = instance.process_of_work.name_project.id  
        instance.delete()
        return redirect(f'/project_detail/{project_id}/')
    
    
class Update_Executor(View):
    
    def get(self,request,executer_id):
        instance = Execute_Process.objects.get(id=executer_id)
        form = CreateExecuter(instance=instance)
        return render(request,'process_create.html',{'form':form})
    
    def post(self,request,executer_id):
        instance = Execute_Process.objects.get(id=executer_id)
        project_id = instance.process_of_work.name_project.id 
        form = CreateExecuter(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect(f'/project_detail/{project_id}/')
        return render(request,'process_create.html',{'form':form})
    