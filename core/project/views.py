from django.shortcuts import render
from django.views import View 
from .models import Detail_Project 
# Create your views here.



class Project_View(View):
    
    
    def setup(self, request, *args, **kwargs):
        self.total_projects = Detail_Project.objects.all()
        return super().setup(request, *args, **kwargs)
    
    def get(self,request):
        
        context = {'total_project':self.total_projects}
        return render(request,'project_list.html',context)
    
    

class Project_View_Detail(View):
    
    
    # def setup(self, request, *args, id , **kwargs):
    #     self.project = Detail_Project.objects.get(id=id)
    #     return super().setup(request, *args,id, **kwargs)
    
    def get(self,request,id):
        self.project=Detail_Project.objects.get(id=id)
        context = {'project':self.project}
        return render(request,'project_detail.html',context)
    
    

