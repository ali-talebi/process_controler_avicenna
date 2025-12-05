from django.db import models
from django.urls import reverse 

# Create your models here.


class Detail_Project(models.Model):
    
    name_project = models.CharField(verbose_name="نام پروژه",max_length=100)
    
    
    def __str__(self):
        return self.name_project 
    
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[self.id,])
    
    class Meta:
        db_table = "Detail_Project"
        verbose_name_plural = "پروژه ها"