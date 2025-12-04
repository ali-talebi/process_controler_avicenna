from django.contrib import admin
from .models import Detail_Project
from process.models import Detail_Process
# Register your models here.




class Process_Inline(admin.StackedInline):
    model = Detail_Process
    extra = 0 
@admin.register(Detail_Project)
class Detail_Project(admin.ModelAdmin):
    list_display = ['name_project', ]
    
    inlines = [Process_Inline]
     