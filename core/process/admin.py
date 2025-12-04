from django.contrib import admin
from .models import Detail_Process , Execute_Process 
# Register your models here.



@admin.register(Execute_Process)
class Execute_Process_Admin(admin.ModelAdmin):
    list_display = ['name_of_work','worker_of_work','process_of_work','time_created','time_update']
    list_filter  = ['worker_of_work','process_of_work'] 
    list_editable = ['process_of_work',]
    

class Process_Executer_Inline(admin.StackedInline):
    model = Execute_Process
    extra = 0


@admin.register(Detail_Process)
class Detail_Process_Admin(admin.ModelAdmin):
    list_display = ['name_project','name_process','creator','time_created','time_update']
    
    
    inlines = [Process_Executer_Inline]

