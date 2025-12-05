from django.urls import path 
from .views import Project_View , Project_View_Detail


app_name = "project"

urlpatterns = [
    path('',Project_View.as_view(),name="project_view"),
    path('project_detail/<int:id>/',Project_View_Detail.as_view(),name="project_detail"),
]
