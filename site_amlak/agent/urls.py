from django.urls import path
from . import views

app_name="agent"

urlpatterns = [
    path("",views.agent_list, name="agent_list"),
    
    path("<int:id>",views.agent_detail, name="agent_detail"),
]
