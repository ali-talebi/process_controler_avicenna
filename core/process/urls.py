from django.urls import path 
from .views import CreateProcess_View ,DeleteProcess_View ,CreateExecuter_View ,DeleteExecuter_View ,Update_Executor


app_name = "process"
urlpatterns = [
    path('create_process/<int:project_id>/',CreateProcess_View.as_view(),name="create_process"),
    path('create_executer/<int:project_id>/<int:process_id>/',CreateExecuter_View.as_view(),name="create_executer"),
    path('delete_executer/<int:executer_id>/',DeleteExecuter_View.as_view(),name="delete_executer"),
    path('delete_process/<int:process_id>/',DeleteProcess_View.as_view(),name="delete_process"),
    path('update_executer/<int:executer_id>/',Update_Executor.as_view(),name="update_exec"),
    
]
