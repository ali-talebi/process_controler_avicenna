from django.db import models

# Create your models here.


class Detail_Project(models.Model):
    
    name_project = models.CharField(verbose_name="نام پروژه",max_length=100)
    
    
    def __str__(self):
        return self.name_project 
    
    class Meta:
        db_table = "Detail_Project"
        verbose_name_plural = "پروژه ها"