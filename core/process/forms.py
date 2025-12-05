from django import forms 
from .models import Detail_Process , Execute_Process 


class CreateExecuter(forms.ModelForm):
    class Meta:
        model = Execute_Process
        fields  = "__all__"

class CreateProcess(forms.ModelForm):
    
    class Meta:
        model = Detail_Process 
        fields = '__all__'

