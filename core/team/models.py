from django.db import models

# Create your models here.


class Member(models.Model):
    
    name_member = models.CharField(verbose_name="نام و نام خانوادگی" , max_length=100)
    picture = models.FileField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name_member 
    
    class Meta:
        db_table = "Member"
        verbose_name_plural = 'اعضای تیم'
        
        
    
    