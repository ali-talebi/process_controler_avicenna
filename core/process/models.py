from django.db import models
from team.models import Member
from project.models import Detail_Project 
# Create your models here.


class Execute_Process(models.Model):
    
    worker_of_work = models.ForeignKey(Member,verbose_name="انجام دهنده فعالیت در این فرایند ",on_delete=models.PROTECT)
    name_of_work = models.CharField(verbose_name="نام عمل اقدام شده" , max_length=100)
    process_of_work = models.ForeignKey('Detail_Process',verbose_name="فرایند مرجع",on_delete=models.PROTECT)
    description_work = models.TextField(verbose_name="متن توضیحات")
    document1_work = models.FileField(verbose_name="سند3 ایجاد شده در این بخش اجرایی" , null=True,blank=True)
    document2_work = models.FileField(verbose_name="سند2 ایجاد شده در این بخش اجرایی" , null=True,blank=True)
    document3_work = models.FileField(verbose_name="سند3 ایجاد شده در این بخش اجرایی" , null=True,blank=True)
    time_created = models.DateTimeField(verbose_name="زمان ایجاد اقدام",auto_now_add=True)
    time_update  = models.DateTimeField(verbose_name="به روزرسانی  زمان اقدام" , auto_now=True) 
    result_work = models.TextField(verbose_name="نتیجه این عمل صورت گرفته" )
    
    
    def __str__(self):
        return f'{self.process_of_work} - {self.name_of_work}'
    
    class Meta:
        db_table = "Execute_Process"
        verbose_name_plural = "ریز اقدامات فرایند ها"
    
    
     

class Detail_Process(models.Model):
    
    name_project = models.ForeignKey(Detail_Project,verbose_name="پروژه مرجع",on_delete=models.PROTECT,null=True)
    name_process = models.CharField(verbose_name="نام فعالیت", max_length=100)
    creator = models.ForeignKey(Member,verbose_name="ایجاد کننده فعالیت",on_delete=models.PROTECT)
    time_created = models.DateTimeField(verbose_name="زمان ایجاد فعالیت",auto_now_add=True)
    time_update  = models.DateTimeField(verbose_name="به روزرسانی فرایند" , auto_now=True) 
    
    def __str__(self):
        return self.name_process
    
    class Meta:
        db_table = "Detail_Process"
        verbose_name_plural = "توضیحات فرایندها"
    